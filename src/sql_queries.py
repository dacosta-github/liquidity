import os 

# DROP TABLES

ads_table_drop = "DROP TABLE IF EXISTS ads;"
replies_table_drop = "DROP TABLE IF EXISTS replies;"
segments_table_drop = "DROP TABLE IF EXISTS segments;"
categories_table_drop = "DROP TABLE IF EXISTS categories;"


# TRUNCATE TABLES
ads_table_truncate = "TRUNCATE TABLE ads"
replies_table_truncate = "TRUNCATE TABLE replies"
segments_table_truncate = "TRUNCATE TABLE segments"
categories_table_truncate = "TRUNCATE TABLE categories"

# CREATE TABLES

ads_table_create = "CREATE TABLE IF NOT EXISTS ads ( date date NOT NULL, \
                                                     user_id INT NOT NULL , \
                                                     ad_id INT NOT NULL, \
                                                     category_id INT not null, \
                                                     params varchar);"

replies_table_create = "CREATE TABLE IF NOT EXISTS replies ( date date NOT NULL, \
                                                             user_id INT NOT NULL , \
                                                             ad_id INT NOT NULL, \
                                                             mail varchar NULL, \
                                                             phone varchar NULL);"

segments_table_create = "CREATE TABLE IF NOT EXISTS segments ( user_id INT NOT NULL , \
                                                        segment VARCHAR NOT NULL);"

categories_table_create = "CREATE TABLE IF NOT EXISTS categories ( category_id INT not null,\
                                                                   category_name VARCHAR);"

# INSERT RECORDS

ads_table_insert = " INSERT INTO ads VALUES(%s, %s, %s, %s, %s);"

#replies_table_insert = " INSERT INTO replies VALUES(%s, %s, %s, NULLIF(%s, '0'), NULLIF(%s, '0'));"
replies_table_insert = " INSERT INTO replies VALUES(%s, %s, %s, %s, %s);"

categories_table_insert = " INSERT INTO categories VALUES(%s, %s);"

segments_table_insert = " INSERT INTO segments VALUES(%s, %s);"


# FIND LIQUIDITY

user_liquidity_select = " with cte_ad_replies as (\
                            select a.user_id,\
                                    count(distinct b.ad_id) as num_ad_replied\
                            from ads a\
                            inner join replies as b\
                                on a.user_id = b.user_id\
                                    and a.ad_id = b.ad_id\
                            where b.date - a.date <= 7\
                            and (\
                                    cast(b.mail as int) >= 1\
                                    or\
                                    cast(b.phone as int) >= 1\
                            )\
                    group by a.user_id\
                ), \
                    cte_ads as (\
                select user_id,\
                            count(1) as num_ads\
                    from ads\
                    group by user_id\
                    )\
                select a.user_id, A.num_ads, B.num_ad_replied, round(((B.num_ad_replied * 1.0) / A.num_ads) * 100, 2) as Liquidity\
                from cte_ads as a\
                join cte_ad_replies as b\
                on A.user_id = B.user_id\
                    order by 4 desc; "

# QUERY LISTS

create_table_queries = [ads_table_create, segments_table_create, categories_table_create, replies_table_create]
drop_table_queries = [ads_table_drop, replies_table_drop, segments_table_drop, categories_table_drop]
truncate_table_queries = [ads_table_truncate, replies_table_truncate, segments_table_truncate, categories_table_truncate]