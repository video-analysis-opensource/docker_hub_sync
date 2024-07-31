# docker_hub_sync
由于国内已经无法拉取dockerhub镜像。<br/>
同步AI开发常用的docker镜像到阿里云镜像仓库，便于在国内快速拉取, 助力开发。<br/>
当前已包含如下镜像:<br/>
pytorch tensorflow rocm-terminal ubuntu centos openjdk

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
- pytorch 同步自dockerhub。 pytorch/pytorch:tag。目前已同步如下镜像
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.1-cuda11.8-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.1-cuda11.8-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.1-cuda12.1-cudnn8-devel 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.1-cuda12.1-cudnn8-runtime 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.0-cuda12.1-cudnn8-devel 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.0-cuda12.1-cudnn8-runtime 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.0-cuda11.8-cudnn8-devel 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.3.0-cuda11.8-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.0.1-cuda11.7-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.0.1-cuda11.7-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.0.0-cuda11.7-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:2.0.0-cuda11.7-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.9.1-cuda11.1-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.9.1-cuda11.1-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.9.0-cuda11.1-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.9.0-cuda11.1-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.9.0-cuda10.2-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.9.0-cuda10.2-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.8.1-cuda11.1-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.8.1-cuda11.1-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.8.1-cuda10.2-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.8.1-cuda10.2-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.8.0-cuda11.1-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.8.0-cuda11.1-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.7.1-cuda11.0-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.7.1-cuda11.0-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.7.0-cuda11.0-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.7.0-cuda11.0-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.6.0-cuda10.1-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.6.0-cuda10.1-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.5.1-cuda10.1-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.5.1-cuda10.1-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.5-cuda10.1-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.5-cuda10.1-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.4-cuda10.1-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.4-cuda10.1-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.3-cuda10.1-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.3-cuda10.1-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.2-cuda10.0-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.2-cuda10.0-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.13.1-cuda11.6-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.13.1-cuda11.6-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.13.0-cuda11.6-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.12.1-cuda11.3-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.12.1-cuda11.3-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.12.0-cuda11.3-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.12.0-cuda11.3-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.11.0-cuda11.3-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.11.0-cuda11.3-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.10.0-cuda11.3-cudnn8-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.10.0-cuda11.3-cudnn8-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.1.0-cuda10.0-cudnn7.5-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.0.1-cuda10.0-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.0.1-cuda10.0-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.0-cuda10.0-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:1.0-cuda10.0-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:0.4_cuda9_cudnn7
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:0.4.1-cuda9-cudnn7-runtime
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:0.4.1-cuda9-cudnn7-devel
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:0.4-cuda9-cudnn7-devel
```
- tensorflow  同步自dockerhub。tensorflow/tensorflow 目前已同步如下镜像
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.17.0-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.17.0-gpu-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.17.0-gpu 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.17.0 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.16.2-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.16.2-gpu-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.16.2-gpu 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.16.2 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.16.1-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.16.1-gpu-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.16.1-gpu 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.16.1 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.15.0-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.15.0-gpu-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.15.0-gpu 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.15.0 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.14.0-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.14.0-gpu-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.14.0-gpu 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.14.0 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.9.1-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.9.1-gpu-jupyter 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.9.1-gpu 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/tensorflow:2.9.1
```
- rocm-terminal  同步自dockerhub。 rocm/rocm-terminal 
当前已包含的镜像：
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/rocm-terminal:5.2
```
- dev-ubuntu-20.04 同步自dockerhub。 rocm/dev-ubuntu-20.04
当前已包含的镜像：
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/dev-ubuntu-20.04:5.2-complete
```
- py38 同步自dockerhub。 zhoukunpeng505/py38
python3.8基础运行环境image， by  zhoukunpeng<br/>
当前已包含的镜像
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/py38:2023-06-16-9f49228
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/py38:2023-06-16-991451c
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/py38:2023-06-15-fb5dcee
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/py38:2023-06-15-ab28ee9
```
- ubuntu 同步自官方源。 ubuntu,当前已包含镜像：
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:oracular 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:oracular-20240617 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:24.10 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:jammy 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:22.04 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:noble 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:24.04 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:23.10 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:22.04 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/ubuntu:20.04  
```
- centos 同步自官方源。 centos,当前已包含：
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/centos:centos7.9.2009 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/centos:centos7 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/centos:centos8.4.2105 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/centos:centos8 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/centos:centos6.10 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/centos:centos6 
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/centos:8.2.2004 
```
- openjdk  同步自官方源。 openjdk 当前已包含：
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/openjdk:8
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/openjdk:11
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/openjdk:17
```
- nginx 同步自官方源。 当前已包括：
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.27
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.27.0
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.26
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.26.1
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.25
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.25.5
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.25.4
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.25.3
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.25.2
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/nginx:1.25.1 
```
- mysql
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mysql:5.6
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mysql:5.7
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mysql:8.0
```
- mariadb
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mariadb:10.8.2
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mariadb:10.8.3
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mariadb:10.8.4
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mariadb:10.8.5
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mariadb:10.8.6
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mariadb:10.8.7
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mariadb:11.1
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/mariadb:11.2
```
- postgis
```bash
registry.cn-hongkong.aliyuncs.com/zhoukunpeng/postgres11_postgis_cube:latest
```
## 问题反馈
如有AI开发相关docker image需要从dockerhub同步，请提交issue，我这边会第一时间处理。