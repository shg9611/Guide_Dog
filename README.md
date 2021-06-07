# Guide_Dog

## 2021-1학기 아주대학교 오픈소스SW 팀 프로젝트

이 프로젝트는 오픈소스SW 전공수업에서 진행한 팀 프로젝트입니다.

Open CV를 활용하며 기존에 존재하는 오픈소스를 활용하여 오픈소스 커뮤니티에 기여하는 것이 목표입니다.

## 소개

해당 오픈소스는 **시각 장애인의 보행권을 보장**하기 위한 시스템의 프로토타입 모델입니다.

**Semantic Segmentation**을 활용하여 **인도**와 **차도**를 구분합니다.

**Object Detection**을 활용하여 시각장애인의 보행에 위협이 될만한 **장애물**을 검출합니다.


## Sample Results

![](docs/imgs/output.jpg) 

Semantic Segmentation Original repository: https://github.com/selectstarofficial/segmentation-selectstar

Object Detection Original repository: https://github.com/ultralytics/yolov5

## Semantic Segmentation Dataset Classes
    
Class | Label | RGB Color
--- | --- | ---
background|0|[0, 0, 0]
bike_lane|1|[255, 128, 0]
caution_zone|2|[255, 0, 0]
crosswalk|3|[255, 0, 255]
guide_block|4|[255, 255, 0]
roadway|5|[0, 0, 255]
sidewalk|6|[0, 255, 0]

## 팀원

<table>
    <tr>
        <td align='center'>Name</td><td align='center'>Github</td><td align='center'>Contact</td>
    </tr>
    <tr>
        <td>홍성빈</td>
        <td><a href="https://github.com/Sophoca"><img src="https://img.shields.io/badge/Sophoca-777?style=social&logo=github"/></td>
        <td><a href="tjdqls1668@gmail.com"><img src="https://img.shields.io/static/v1?label=&message=tjdqls1668@gmail.com&color=white&style=flat-square&logo=gmail"></td>
    </tr>
    <tr>
        <td>신호근</td>
        <td><a href="https://github.com/shg9611"><img src="https://img.shields.io/badge/shg9611-777?style=social&logo=github"/></td>
        <td><a href="shg9611@naver.com"><img src="https://img.shields.io/static/v1?label=&message=shg9611@naver.com&color=white&style=flat-square&logo=naver"></td>
    </tr>
    <tr>
        <td>김영진</td>
        <td><a href="https://github.com/jin-Pro"><img src="https://img.shields.io/badge/jin_Pro-777?style=social&logo=github"/></td>
        <td><a href="dnjun2@naver.com"><img src="https://img.shields.io/static/v1?label=&message=dnjun2@naver.com&color=white&style=flat-square&logo=naver"></td>
    </tr>
</table>

   
## 실행 방법

#### 1. Install python packages
    ```
    Install Anaconda3 [https://www.anaconda.com/distribution/]
    conda create ml
    conda activate ml
    conda install conda
    conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
    pip install tensorboardx, matplotlib
    ```
    
#### 2. Download pretrained model

[Model Weights](https://drive.google.com/file/d/1Y8RhV3hWEoE4mqbriGbAyMDQMIaQdrnb/view?usp=sharing)

Download and put it into ```./run/surface/deeplab/model_iou_77.pth.tar```

#### 3. Prepare 'mp4 video' to predict

Put it into 'test' directory

#### 4. Edit settings
Edit ```RUN OPTIONS``` on predict.py
    ```
    MODEL_PATH, MODE, DATA_PATH, OUTPUT_PATH
    ```

#### 5. Run ```predict.py```

