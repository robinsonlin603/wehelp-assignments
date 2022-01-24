要求二
descbire `member`;

![要求二](https://user-images.githubusercontent.com/93252094/150737518-586ca6eb-a900-48aa-9274-d12f0a2b3cf3.jpeg)

要求三
1.取得所有會員資料
SELECT * FROM `member`;
![要求3-1](https://user-images.githubusercontent.com/93252094/150737661-19af00ca-e82c-4f57-a8dd-4d90ca651b0a.jpeg)

2.按照time排列,近到遠
SELECT * FROM `member` ORDER BY `time` DESC ;
![要求3-2](https://user-images.githubusercontent.com/93252094/150737773-1934b5e5-5f86-434a-8c97-b3b8b8e2f386.jpeg)

3.取 第二到四 共三筆資料
SELECT * FROM `member` ORDER BY `time` DESC LIMIT 2,4;
![要求3-3](https://user-images.githubusercontent.com/93252094/150737894-25184c1b-4825-484c-8f68-6985cc4e3749.jpeg)

4.取test的會員資料
SELECT * FROM `member` WHERE `username`='test';
![要求3-4](https://user-images.githubusercontent.com/93252094/150737989-6c252426-fa73-497f-ae0e-14bac633e3a1.jpeg)

5.取得username與password是test的會員資料
SELECT * FROM `member` WHERE `username`='test' AND `password`='test';
![要求3-5](https://user-images.githubusercontent.com/93252094/150738115-8d554d71-396d-465d-a502-6e4c3a684a86.jpeg)

6.把username=test的會員,name改成test2
UPDATE `member` SET `name`='test2' WHERE `username`='test';
![要求3-6](https://user-images.githubusercontent.com/93252094/150738258-0aee32ce-45ac-4836-90fb-7768a21e7e98.jpeg)

要求四
1.共幾筆資料
SELECT COUNT(*) FROM `member`; 
![要求4-1](https://user-images.githubusercontent.com/93252094/150738380-4a1bafa5-b036-4ef7-872b-39c52163b740.jpeg)

2.follower_count 總和
SELECT SUM(`follower_count`) FROM `member`;
![要求4-2](https://user-images.githubusercontent.com/93252094/150738385-4bf0a1b7-8904-440f-b45e-63b722d15fd5.jpeg)

3.follower_avg 平均
SELECT AVG(`follower_count`) FROM `member`;
![要求4-3](https://user-images.githubusercontent.com/93252094/150738550-c38d500a-5d5e-431e-9cca-bd4aef486664.jpeg)

要求五
1.取得所有留言
SELECT `member`.`name`,`message`.`content`,`message`.`time` FROM `member` JOIN `message` ON `message`.`member_id`=`member`.`id`;
![要求5-1](https://user-images.githubusercontent.com/93252094/150738772-e9295014-8643-4eb1-abf6-b7177b5b81fb.jpeg)

2.所得test所有留言
SELECT `member`.`name`,`message`.`content`,`message`.`time` FROM `member` JOIN `message` ON `message`.`member_id`=`member`.`id` AND `member`.`username`='test';
![要求5-2](https://user-images.githubusercontent.com/93252094/150738837-aee9f0ee-709b-420b-b3ad-36fdaebf71cc.jpeg)

