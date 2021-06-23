## Protocol
+ 컴퓨터나 네트워크 장비가 서로 통신하기 위해 미리 정해 놓은 약속, 규약

## SSH
+ 암호화된 네트워크 프로토콜
	+ 일반적으로 암호화 하지 않는 네트워크 위에서 암호화된 접속 및 서비스 사용을 위해 사용

#### Linux SSH
<pre>
<code>
1.
$ ssh user@hostname
2.
$ ssh user@127.0.0.1
</code>
</pre>
+ 일반적인 커멘드는 다음과 같다. 접속에 성공한다면 그 때부터 원격 호스트의 쉘을 사용하게 된다.
+ [ssh directory](https://jdm.kr/blog/212)

## RSA fingerprint
+ host key fingerprint 라고도 불린다.
+ SSH 서버(server)는 host key를 통해 클라이언트(client)가 host에 연결되었는지 확인한다.


# Answer
<p align="center"><img src="https://user-images.githubusercontent.com/37611500/123123564-e3a45700-d481-11eb-8f33-ff224214647a.PNG">
	
<p align="center"><img src="https://user-images.githubusercontent.com/37611500/123123938-33831e00-d482-11eb-81cf-3d1a07867b3c.PNG">

Answer(flag) : mommy! I think I know what a file descriptor is!!
