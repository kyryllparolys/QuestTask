-- Postgres syntax
    create table products(
        id serial primary key ,
        name varchar(50) not null,
        price integer not null
    );

    create table tags(
        id serial primary key,
        name varchar(50) not null,
    );

    create table products_tags(
        product_id int references products(id) on update cascade on delete cascade,
        tag_id int references tags(id) on update cascade on delete cascade,
        CONSTRAINT id PRIMARY KEY (product_id, tag_id)
    );

    SELECT
        products.id,
        products.name,
        products.price
    FROM products
    INNER
        JOIN products_tags
        ON products.id = products_tags.product_id
    GROUP by products.id
    HAVING COUNT(products.id) > 10;