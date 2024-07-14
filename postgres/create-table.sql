create table sentences (
    id serial primary key,
    sentence varchar(10000) not null,
    sentiment float
)