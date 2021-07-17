## Answer

![Alt text](https://user-images.githubusercontent.com/37611500/126041094-ff154499-2fe3-4eee-8037-f559e76e2827.PNG)
+ hashcode 변수와 비교
+ 5번 더한 값이 hashcode와 동일해야 함

#### ps
+ intel 방식의 Little Endian 방식
+ chck_password함수 인자로 char값을 받았지만, int 형 변환이 이루어져 for문내에서 1씩 증가할 때마다 4byte씩 받아오게 된다.
