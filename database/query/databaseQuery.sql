CREATE DATABASE bdoctordb;
use bdoctordb;

create table doctorInfor (
	UUID varchar(36),
    familyname varchar(50),
    lastname varchar(50),
    address varchar(100),
    email varchar(50),
    phone varchar(10),
    medicalmajor varchar(124),
    avatarURL varchar(124),
    birthyear year,
    hometown varchar(512),
    currentWorkingLocation varchar(512),
    education varchar(512),
    primary key (UUID),
    FOREIGN KEY (UUID) REFERENCES accountInfor(UUID)
);
create table doctorExperience (
	UUID varchar(36),
    description varchar(512),
    inTime int,
	primary key (UUID),
    FOREIGN KEY (UUID) REFERENCES accountInfor(UUID)
);
create table doctorAchiverment (
	UUID varchar(36),
    description varchar(512),
    inTime year,
	primary key (UUID),
    FOREIGN KEY (UUID) REFERENCES accountInfor(UUID)
);
create table accountInfor (
	UUID varchar(36),
    username varchar(32),
    password varchar(512),
    role int,
    date_create date,
    date_edit date,
    /* Account role
		admin 	0
        user 	1
        staff 	2
        */
	primary key (UUID),
    unique (username)
);
create table initAccount (
	UUID varchar(36),
    username varchar(32),
    password varchar(512),
    changingstatus boolean default false,
	primary key (UUID),
    foreign key (UUID) references accountinfor(UUID),
    unique (username)
);














CREATE TABLE Patient (
    ID int auto_increment,
    ResidentNumber varchar(12),
    HealthInsuranceID varchar(20),
    PatientName varchar(50),
    birthyear year,
    gender boolean,
    job varchar(50),
    address varchar(100),
    primary key (ID)
);

create table XrayImage (
	ID int auto_increment,
    patientID int,
    URLimage varchar(100),
    imagetime date,
    symtom text,
    imagedirection boolean,
    imageside boolean,
    primary key (ID),
    FOREIGN KEY (patientID) references Patient(ID)
);
create table ImpXrayImage (
	ID int auto_increment,
    URLimage varchar(512),
    ImgName varchar(125),
    patientID int,
    primary key (ID),
    FOREIGN KEY (patientID) references Patient(ID)
);
create table PatientHospitalizeInfor (
	ID int auto_increment,
    patientID int,
    hospitalizeTime date,
    hospitalizeLocation varchar(1024),
    hospitalizeSymptom varchar(1024),
    primary key (ID),
    FOREIGN KEY (patientID) references Patient(ID)
);accountinfor

insert into PatientHospitalizeInfor(ID, patientID, hospitalizeTime, hospitalizeLocation, hospitalizeSymptom)
	VALUES (null, 30, '2020-9-17', "abd", "abc")