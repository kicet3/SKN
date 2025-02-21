#DML
SELECT menu_code,menu_name,menu_price,category_code,orderable_status FROM tbl_menu;

#INSERT

INSERT INTO tbl_menu VALUES(null,'곰탕',9500,6,'Y');

INSERT INTO tbl_menu(menu_code,menu_name,menu_price,orderable_status,category_code)
VALUES (null,'차돌짬뽕',15000,'Y',6);


#UPDAte
-- UPDATE 테이블명
-- SET 컬럼명1 = 수정할 데이터,
--     컬럼명2 = 수정할 데이터,
--     ...
-- [WHERE 수정 대상 데이터 조건 ];

UPDATE tbl_menu SET menu_name = '100번이었던 음식', menu_price=19000 WHERE menu_code=100;
-- SAFE UPDAE MODE가 설정되어 있으면 WHERE 절 없이 수정이 불가능함.

SELECT * FROM tbl_menu;

INSERT INTO tbl_menu(menu_code,menu_name,menu_price,orderable_status,category_code)
VALUES (null,'몰라',15000,'Y',100);

DELETE FROM tbl_menu WHERE menu_code=101;

REPLACE INTO tbl_menu VALUES (100,'100번 음식 REPLACE',100,10,'Y');

SELECT * FROM tbl_menu;
REPLACE tbl_menu VALUES(120,'없는 메뉴 REPLACE',11111,8,'Y');



