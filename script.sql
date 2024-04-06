create database shape24;
use shape24;


create table users (
    user_id int,
    email varchar(255),
    password varchar(255),
    primary key(user_id, email)
);

insert into users values(100, 'test@gmail.com', '1234');

create table projects (
    project_id integer,
    project_title varchar(500),
    availability integer,
    primary key(project_id, project_title)
);

insert into projects values(122133, 'Project 1', 2);
insert into projects values(122134, 'Project 2', 2);
insert into projects values(122135, 'Project 3', 2);

create table assigned_projects(
    user_id int,
    project_id int,
    foreign key(user_id) references Users(user_id),
    foreign key(project_id) references projects(project_id),
    primary key(user_id, project_id)
);

alter table assigned_projects add constraint unique_user_id unique(user_id);

