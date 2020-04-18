-- Postgres syntax
    create table products(
        id serial primary key ,
        name varchar(50) not null,
        price integer not null
    );

    create table tags(
        id serial primary key,
        name varchar(50) not null,
        product_id integer not null,
        foreign key(product_id) references products(id) on delete cascade
    );

    SELECT
        products.id,
        products.name,
        products.price,
        tags.product_id
    FROM products
    INNER
        JOIN tags
        ON products.id = tags.product_id
    GROUP by products.id, tags.product_id
    HAVING COUNT(tags.product_id) > 10;