create database shape24;
use shape24;


create table users (
    user_id int,
    email varchar(255),
    password varchar(255),
    primary key(user_id, email)
);

insert into users values(100, 'test@gmail.com', '1234');
insert into users values(101, 'test1@gmail.com', '1234');

create table projects (
    project_id integer,
    project_title varchar(500),
    availability integer,
    primary key(project_id, project_title)
);

create table assigned_projects(
    user_id int,
    project_id int,
    foreign key(user_id) references Users(user_id),
    foreign key(project_id) references projects(project_id),
    primary key(user_id, project_id)
);

alter table assigned_projects add constraint unique_user_id unique(user_id);

alter table projects add column description text, add column sdg text, add column faculty_name text, add column college_email text, add column mobile_number text, add column department text;

alter table assigned_projects add column allotment_time text;

insert into projects (project_id,faculty_name,college_email,mobile_number,department,project_title,description,sdg,availability) values
("1011","Dr.Divya B","divysb@ssn.edu.in","9952068826","BME","EEG for cognitve load analysis","EEG offers a direct, real-time window into brain activity, making it a powerful tool for measuring cognitive load by detecting changes in brainwave patterns associated with mental effort. This capability allows for the optimization of learning materials, work environments, and user interfaces by tailoring them to human cognitive capacities.","SDG 3 - Good Health and Well-Being",1),
("1022","Dr. Srinath Rajagopalan","srinathr@ssn.edu.in","9962515971","Civil",I"ntegrating Waste Quarry Dust Sludge and Agro Wastes in Fireless Brick Manufacturing","To explore the feasibility of utilizing waste quarry dust sludge and agro wastes in fireless brick production, aiming to enhance brick strength, durability, and environmental sustainability. Investigate the properties of waste materials, conduct laboratory tests on brick samples, and assess the economic and environmental feasibility of the proposed approach. Expected Outcome: Development of a sustainable and cost-effective method for fireless brick manufacturing.","SDG 9 - Industry, Innovation, and Infrastructure",1),
("1138","Dr. Surendar Natarajan","surendarn@ssn.edu.in","9444432583","Civil","Groundwater Quality Management ","Ground water is a major source of water resources for drinking and irrigation purposes. Rapid urbanization and expansion of agricultural land leads to groundwater exploitation which deteriorates the groundwater quality. This study focuses on analyzing the groundwater quality in near by regions of their interest. ","SDG 14: Life Below Water",1);

commit;