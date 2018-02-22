cloud vm provision playbook
======

For provisioning cloud vm using ansible playbook(only openstack, aws)

# Requirement
ansible 2.3+  
aws sdk for python(boto) 

# Info
## inventory
- inventory/inventory.cfg

## variabes
> inventory/group_var/localhost.yml
 - cloud provider 접속정보 입력
 - 생성하고 싶은 노드 개수 입력

## play
> init.yml
 - provider(openstack, aws) 선택확인
 - 각 role실행

## roles
> roles
 - vm 생성(ec2, nova) 
 - docker(or rkt) 설치(docker)
 - 필수 패키지 설처(bootstrap-os)
 - 접속정보 수집(예정)
 - kubespray용 인벤토리 생성(예정)

# 개선할 내용
- 접속 정보 수집
- kubespray용 inventory생성
- ansible-vault 이용하여 password, access key 암호화
