<template>
    <div>
        <div id="container" style="position: relative">
            <video id="camera" autoplay :style="cameraStyle"></video>
        </div>
        <h4 id="log" :style="labelStyle"></h4>
        <Button type="success" long @click="register">确认录入</Button>
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
                type: String
            },
            password: {
                type: String
            },
            Snum: {
                type: String
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
                const camera = document.getElementById('camera');
                camera.hidden = true;
                const log = document.getElementById('log');
                log.innerText = '加载模型中，请稍后';
                const MODEL_URL = '/models';
                Promise.all([
                    faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL),
                    faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL),
                    faceapi.nets.ssdMobilenetv1.loadFromUri(MODEL_URL),
                    faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL),
                    faceapi.nets.faceExpressionNet.loadFromUri(MODEL_URL)
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
                        const detections = await faceapi.detectAllFaces('camera').withFaceLandmarks().withFaceDescriptors().withFaceExpressions();
                        const resizeDetections = faceapi.resizeResults(detections, displaySize);
                        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
                        faceapi.draw.drawDetections(canvas, resizeDetections);
                        faceapi.draw.drawFaceExpressions(canvas, resizeDetections);
                        if (detections.length === 1) {
                            this.onCheckSuccess(resizeDetections[0].descriptor);
                            log.innerText = '人脸检测成功'
                        } else if (detections.length < 1) {
                            log.innerText = '未检测到人脸'
                        } else if (detections.length > 1) {
                            log.innerText = '多个人脸出现在摄像头中！'
                        }
                    }, this.delay)
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
                this.face_vector = distance.toString()
            },
            onCheckFailed(distance) {
                if (!this.failed) {
                    this.failed = true;
                }
            },
            register() {
                if (this.face_vector) {
                    let data = {
                        username: this.username,
                        password: this.password,
                        face_vector: this.face_vector,
                    };
                    this.$api.user.update_api(data).then(res => {
                        if (res.data.code === 1) {
                            this.$emit('success');
                            const camera = document.getElementById('camera');
                            camera.srcObject.getTracks()[0].stop();
                            clearInterval(this.timer);
                        }
                    });
                }
            }
        },
        data() {
            return {
                counter: 0,
                timer: undefined,
                failed: false,
                success: false,
                face_vector: ''
            }
        },
        mounted() {
            this.initFaceApi()
        }
    }
</script>

<style scoped>
    video {
    }

    >>> canvas {
        position: absolute;
        z-index: 999;
        left: 0;
    }
</style>
