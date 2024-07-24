# docker_hub_sync
由于国内已经无法拉取dockerhub镜像。<br/>
同步AI开发常用的docker镜像到阿里云镜像仓库，便于在国内快速拉取, 助力开发。<br/>
当前已包含如下镜像:<br/>
pytorch tensorflow rocm-terminal ubuntu centos

## 1. 说明
每日同步从dockerhub同步一次，准实时和官方保持一致。<br/>
使用方式：
```bash
docker pull registry.cn-hongkong.aliyuncs.com/zhoukunpeng/[镜像名]:[镜像版本号]
```
```bash
# 如：pytorch
docker pull registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.1-cuda11.8-cudnn8-devel
```
## 2. 当前包含的镜像
- pytorch 同步自dockerhub。 pytorch/pytorch:tag。目前已同步如下版本
```bash
2.3.1-cuda11.8-cudnn8-devel
2.3.1-cuda11.8-cudnn8-runtime
2.3.1-cuda12.1-cudnn8-devel 
2.3.1-cuda12.1-cudnn8-runtime 
2.3.0-cuda12.1-cudnn8-devel 
2.3.0-cuda12.1-cudnn8-runtime 
2.3.0-cuda11.8-cudnn8-devel 
2.3.0-cuda11.8-cudnn8-runtime
2.0.1-cuda11.7-cudnn8-runtime
2.0.1-cuda11.7-cudnn8-devel
2.0.0-cuda11.7-cudnn8-runtime
2.0.0-cuda11.7-cudnn8-devel
1.9.1-cuda11.1-cudnn8-runtime
1.9.1-cuda11.1-cudnn8-devel
1.9.0-cuda11.1-cudnn8-runtime
1.9.0-cuda11.1-cudnn8-devel
1.9.0-cuda10.2-cudnn7-runtime
1.9.0-cuda10.2-cudnn7-devel
1.8.1-cuda11.1-cudnn8-runtime
1.8.1-cuda11.1-cudnn8-devel
1.8.1-cuda10.2-cudnn7-runtime
1.8.1-cuda10.2-cudnn7-devel
1.8.0-cuda11.1-cudnn8-runtime
1.8.0-cuda11.1-cudnn8-devel
1.7.1-cuda11.0-cudnn8-runtime
1.7.1-cuda11.0-cudnn8-devel
1.7.0-cuda11.0-cudnn8-runtime
1.7.0-cuda11.0-cudnn8-devel
1.6.0-cuda10.1-cudnn7-runtime
1.6.0-cuda10.1-cudnn7-devel
1.5.1-cuda10.1-cudnn7-runtime
1.5.1-cuda10.1-cudnn7-devel
1.5-cuda10.1-cudnn7-runtime
1.5-cuda10.1-cudnn7-devel
1.4-cuda10.1-cudnn7-runtime
1.4-cuda10.1-cudnn7-devel
1.3-cuda10.1-cudnn7-runtime
1.3-cuda10.1-cudnn7-devel
1.2-cuda10.0-cudnn7-runtime
1.2-cuda10.0-cudnn7-devel
1.13.1-cuda11.6-cudnn8-runtime
1.13.1-cuda11.6-cudnn8-devel
1.13.0-cuda11.6-cudnn8-runtime
1.12.1-cuda11.3-cudnn8-runtime
1.12.1-cuda11.3-cudnn8-devel
1.12.0-cuda11.3-cudnn8-runtime
1.12.0-cuda11.3-cudnn8-devel
1.11.0-cuda11.3-cudnn8-runtime
1.11.0-cuda11.3-cudnn8-devel
1.10.0-cuda11.3-cudnn8-runtime
1.10.0-cuda11.3-cudnn8-devel
1.1.0-cuda10.0-cudnn7.5-runtime
1.1.0-cuda10.0-cudnn7.5-devel
1.0.1-cuda10.0-cudnn7-runtime
1.0.1-cuda10.0-cudnn7-devel
1.0-cuda10.0-cudnn7-runtime
1.0-cuda10.0-cudnn7-devel
0.4_cuda9_cudnn7
0.4.1-cuda9-cudnn7-runtime
0.4.1-cuda9-cudnn7-devel
0.4-cuda9-cudnn7-devel
```
- rocm-terminal  同步自dockerhub。rocm/rocm-terminal
当前已包含的版本：
```bash
5.2
```
- dev-ubuntu-20.04 同步自dockerhub。 rocm/dev-ubuntu-20.04
当前已包含的版本：
```bash
5.2-complete
```
- py38 同步自dockerhub。 zhoukunpeng505/py38
python3.8基础运行环境image， by  zhoukunpeng<br/>
当前已包含的版本
```bash
2023-06-16-9f49228
2023-06-16-991451c
2023-06-15-fb5dcee
2023-06-15-ab28ee9
```
- ubuntu 同步自官方源。 ubuntu,当前已包含版本：
```bash
oracular 
oracular-20240617 
24.10 
jammy 
22.04 
noble 
24.04 
23.10 
22.04 
20.04  
```
- centos 同步自官方源。 centos,当前已包含版本：
```bash
centos7.9.2009 
centos7 
centos8.4.2105 
centos8 
centos6.10 
centos6 
8.2.2004 
```
## 问题反馈
如有AI开发相关docker image需要从dockerhub同步，请提交issue，我这边会第一时间处理。
