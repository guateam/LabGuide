<template>
    <div>
        <div id="container" style="position: relative">
            <video id="camera" autoplay :style="cameraStyle"></video>
        </div>
        <h4 id="log" :style="labelStyle"></h4>
    </div>
</template>

<script>
    // import nodejs bindings to native tensorflow,
    // not required, but will speed up things drastically (python required)
    import '@tensorflow/tfjs';

    // implements nodejs wrappers for HTMLCanvasElement, HTMLImageElement, ImageData

    import * as faceapi from 'face-api.js';

    export default {
        name: "FaceCheck",
        props: {
            username: {
                require: true
            },
            password: {
                require: true
            },
            vector: {
                require: true
            },
            limitTime: {
                type: [Number, String],
                default: 1000
            },
            passRate: {
                type: Number,
                default: 0.4
            },
            delay: {
                type: Number,
                default: 100
            },
            modelDelay: {
                type: Number,
                default: 300
            },
            cameraStyle: {
                type: String,
                default: 'max-width: 100%;height: auto;border-radius: 5px'
            },
            labelStyle: {
                type: String,
                default: ''
            }
        },
        watch: {},
        methods: {
            async initFaceApi() {
                this.phone = this.is_phone();
                const camera = document.getElementById('camera');
                camera.hidden = true;
                const log = document.getElementById('log');
                log.innerText = '加载模型中，请稍后';
                const MODEL_URL = '/models';
                Promise.all([
                    faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL),
                    faceapi.nets.faceLandmark68TinyNet.loadFromUri(MODEL_URL),
                    // faceapi.nets.ssdMobilenetv1.loadFromUri(MODEL_URL),
                    // faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL),
                    // faceapi.nets.faceExpressionNet.loadFromUri(MODEL_URL),
                    faceapi.loadTinyFaceDetectorModel(MODEL_URL)
                ]).then(this.getFace)
            },
            initCamera(faceDetections) {
                const log = document.getElementById('log');
                log.innerText = '正在启动摄像头';
                const camera = document.getElementById('camera');
                navigator.getUserMedia({video: {}}, stream => camera.srcObject = stream, error => {
                    throw 'can not load media' + error
                });
                camera.addEventListener('play', () => {
                    log.innerText = '摄像头已启动';
                    camera.hidden = false;
                    const container = document.getElementById('container');
                    const canvas = faceapi.createCanvasFromMedia(camera);
                    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
                    const displaySize = {width: camera.offsetWidth, height: camera.offsetHeight};
                    faceapi.matchDimensions(canvas, displaySize);
                    container.append(canvas);
                    let that = this;
                    this.timer = setInterval(async () => {
                        const useTinyModel = true;
                        const detections = await faceapi.detectAllFaces('camera',new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks(useTinyModel).withFaceDescriptors();
                        const resizeDetections = faceapi.resizeResults(detections, displaySize);
                        if (!that.phone) {
                            canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
                            console.info(resizeDetections);
                            faceapi.draw.drawDetections(canvas, resizeDetections);
                            // faceapi.draw.drawFaceExpressions(canvas, resizeDetections);
                        }
                        if (detections.length === 1 && !that.success && !that.failed) {

                            if (faceDetections !== undefined) {
                                let distance = await faceapi.euclideanDistance(resizeDetections[0].descriptor, faceDetections);

                                log.innerText = '欧几里得度量：' + Math.round((distance) * 100) / 100;
                                // faceapi.draw.drawFaceLandmarks(canvas, resizeDetections);
                                that.counter++;
                                if (distance < that.passRate) {
                                    log.innerText = '验证成功';
                                    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
                                    this.onCheckSuccess(resizeDetections[0].descriptor);
                                    // clearInterval(that.timer);
                                }
                                if (that.counter > that.limitTime) {
                                    log.innerText = '超过比对次数上限，验证失败';
                                    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
                                    that.onCheckFailed(distance);
                                    clearInterval(that.timer);
                                }
                            }
                        } else if (detections.length < 1) {
                            log.innerText = '未检测到人脸'
                        } else if (detections.length > 1) {
                            log.innerText = '多个人脸出现在摄像头中！'
                        }
                    }, this.phone ? 200 : this.delay)
                })
            },
            async getFace() {
                const log = document.getElementById('log');
                log.innerText = '模型已加载，正在加载人脸模板';
                let that = this;
                setTimeout(async () => {
                    that.initCamera(that.vector);
                }, this.modelDelay)

            },
            onCheckSuccess(distance) {
                if (!this.success) {
                    this.success = true;
                    let data = {
                        username: this.username,
                        password: this.password,
                        face_vector: distance.toString()
                    };
                    this.$api.user.login(data).then(res => {
                        if (res.data.code === 1) {
                            import("js-cookie").then(Cookies => {
                                Cookies.set("token", res.data.data.token);
                                Cookies.set("group", 0);
                                this.$store.commit("save", res.data.data);
                                this.$store.commit("update_token", res.data.data.token);
                                const camera = document.getElementById('camera');
                                camera.srcObject.getTracks()[0].stop();
                                clearInterval(this.timer);
                                this.$router.push({name: "default"});
                            });
                        }
                    })
                }

            },
            onCheckFailed(distance) {
                if (!this.failed) {
                    this.failed = true;
                }
            },
            is_phone() {
                let userAgentInfo = navigator.userAgent;
                let Agents = ["Android", "iPhone",
                    "SymbianOS", "Windows Phone",
                    "iPad", "iPod"];
                let flag = false;
                for (let v = 0; v < Agents.length; v++) {
                    if (userAgentInfo.indexOf(Agents[v]) > 0) {
                        flag = true;
                        break;
                    }
                }
                return flag;
            }
        },
        data() {
            return {
                counter: 0,
                timer: undefined,
                failed: false,
                success: false,
                phone: false
            }
        },
        mounted() {
            this.initFaceApi()
        }
    }
</script>

<style scoped>
    video {
        position: absolute;
        z-index: -1;
    }

    >>> canvas {
        z-index: 999;
    }
</style>
