새로운 테이블 생성

CREATE TABLE ORDER_LIST(

    ORDER_DATE  CHAR(8) NOT NULL,

    PRODUCT     VARCHAR2(10) NOT NULL,

    QTY         NUMBER NOT NULL,

    AMOUNT      NUMBER NOT NULL

);



CREATE TABLE SALES_PER_DATE(

    SALE_DATE   CHAR(8) NOT NULL,

    PRODUCT     VARCHAR2(10) NOT NULL,

    QTY         NUMBER NOT NULL,

    AMOUNT      NUMBER NOT NULL



);


create or replace trigger summary_sales
  after insert
  on order_list
  for each row
  declare
   o_date order_list.order_date%type;
   o_prod order_list.product%type;
   begin
   o_date := :new.order_date;
   o_prod := :new.order_prod;
   update sales_per_date
    set qty = qty + :new.qty;
      amount = amount + :new.amout
    where sale_date =o_date
      and product = o_prod;
     if sql%notfound then
      insert into sales_per_date
      values(o_date, o_prod, :new.qty, :new.amount);
      end if;
      end;
      
