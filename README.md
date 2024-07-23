# docker_hub_sync
同步AI开发常用的docker镜像到阿里云镜像仓库，便于在国内快速拉取镜像,相比于从官方拉取速度提高N倍且更加稳定。

## 1. pytorch
每日同步从dockerhub同步一次，准实时和官方保持一致。使用方式：
```bash
docker pull registry.cn-hongkong.aliyuncs.com/zhoukunpeng/pytorch:[镜像版本号]
```
当前已包含的版本：(截止2024-7-23)
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
## 2. rocm/rocm-terminal
```bash
docker pull registry.cn-hongkong.aliyuncs.com/zhoukunpeng/rocm-terminal:[镜像版本号]
```
当前已包含的版本：(截止2024-7-23)
```bash
5.2
```
## 3. rocm/dev-ubuntu-20.04
```bash
docker pull registry.cn-hongkong.aliyuncs.com/zhoukunpeng/rocm-terminal:[镜像版本号]
```
当前已包含的版本：(截止2024-7-23)
```bash
5.2-complete
```
