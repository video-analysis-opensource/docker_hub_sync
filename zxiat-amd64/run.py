# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/7/21
import os
import sys
import json
import requests
import copy
try:
    from aliyunsdkcore.client import AcsClient
    from aliyunsdkcore.request import CommonRequest
    from aliyunsdkcore.auth.credentials import AccessKeyCredential
    from aliyunsdkcore.auth.credentials import StsTokenCredential
except ImportError:
    pass

def get_dockerhub_tags(image_name, platform='amd64', with_digest=False):
    "获取dockerhub中某镜像的TAG list"
    image_tags = requests.get(f'https://hub.docker.com/v2/repositories/{image_name}/tags/?'
                              'page_size=100&page=1&name&ordering').json()
    result = []
    for i in copy.deepcopy(image_tags.get("results", [])):
        if i:
            tag_name = i['name']
            _ = dict([(j['architecture'], j['digest'].lstrip("sha256:")) for j in i['images']])
            if platform in _:
                if with_digest:
                    result.append((tag_name, _[platform]))
                else:
                    result.append(tag_name)
    return result


def get_aliyun_tags(image_name, platform='amd64', with_digest=False):
    "获取阿里云中镜像的TAG list"
    credentials = AccessKeyCredential(key_id, key_secret)
    client = AcsClient(region_id=reign, credential=credentials)
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_method('GET')
    request.set_protocol_type('https')  # https | http
    request.set_domain(api_domain)
    request.set_version('2016-06-07')
    request.add_header('Content-Type', 'application/json')
    request.add_query_param('PageSize', '100')
    #print('url', f'/repos/{image_name}/tags')
    request.set_uri_pattern(f'/repos/{image_name}/tags')
    body = '''{}'''
    request.set_content(body.encode('utf-8'))
    try:
        response = client.do_action_with_exception(request)
        # python2:  print(response)
        response = json.loads(str(response, encoding='utf-8'))
        #print(response)
        result = []
        for i in response['data']['tags']:
            if with_digest:
                result.append((i['tag'], i['digest']))
            else:
                result.append(i['tag'])
        return result
    except Exception as e :
        print(('Except', str(e)))
        return []


def run_cmd(cmd):
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    key_id, key_secret = sys.argv[-2:]
    key_id = key_id.strip()
    key_secret = key_secret.strip()
    reign = 'cn-hongkong'
    api_domain = 'cr.cn-hongkong.aliyuncs.com'
    domain = 'registry.cn-hongkong.aliyuncs.com'
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(current_dir, "config.txt"), 'r') as f:
        config_info = f.readlines()
    config_info = [i.strip().split() for i in config_info]
    config_info = [i for i in config_info if i]
    print(config_info)
    # raise
    for source_image,target_image in config_info:
        if ':' in source_image and ':' in target_image:
            # 带tag
            # 先判断此tag是否已存在
            _0, _1 = target_image.split(":")
            res_aliyun = get_aliyun_tags(_0)
            print("res_aliyun", res_aliyun, _0, _1)
            if _1 not in res_aliyun:
                run_cmd(f"docker pull {source_image}")
                run_cmd(f"docker tag {source_image} {domain}/{target_image}")
                run_cmd(f"docker push {domain}/{target_image}")
                run_cmd(f"docker rmi {source_image}")
                run_cmd(f"docker rmi {domain}/{target_image}")
                pass
        if ':' not in source_image and ':' not in target_image:
            print(source_image,target_image)
            res_dockerhub = get_dockerhub_tags(source_image)
            res_aliyun = get_aliyun_tags(target_image)
            for tag in res_dockerhub:
                if tag != 'latest':
                    if tag not in res_aliyun:
                        run_cmd(f"docker pull {source_image}:{tag}")
                        run_cmd(f"docker tag {source_image}:{tag} {domain}/{target_image}:{tag}")
                        run_cmd(f"docker push {domain}/{target_image}:{tag}")
                        run_cmd(f"docker rmi {source_image}:{tag}")
                        run_cmd(f"docker rmi {domain}/{target_image}:{tag}")

            if 'latest' in res_dockerhub:
                run_cmd(f"docker pull {source_image}:latest")
                run_cmd(f"docker tag {source_image}:latest {domain}/{target_image}:latest")
                run_cmd(f"docker push {domain}/{target_image}:latest")
                run_cmd(f"docker rmi {source_image}:latest")
                run_cmd(f"docker rmi {domain}/{target_image}:latest")