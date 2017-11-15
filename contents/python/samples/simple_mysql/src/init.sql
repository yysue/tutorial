

create table user (
    id int(11) not null AUTO_INCREMENT,
    name varchar(100) default null,
    primary key (id)
) engine=innodb auto_increment=9 default charset='utf8';

insert into user(name) values 
('a'), 
('b'),
('c'),
('d'),
('e'),
('f'),
('h')
;


create table account (
    accid int(11) default null comment '账户ID',
    money int(11) default null comment '余额',
    primary key (accid)
) engine=innodb auto_increment=9 default charset='utf8';

insert into account (accid, money) values
(11, 123),
(12, 99)
;