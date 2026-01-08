DROP VIEW IF EXISTS all_raw_listings_view CASCADE;

--creating a view of 5 raw data tables
CREATE VIEW all_raw_listings_view AS
--getting data from raw_q3_2024 table
SELECT
    host_id, 
    host_name,
    host_since,
    host_location,
    host_about,
    host_response_time,
    host_response_rate,
    host_acceptance_rate,
    host_is_superhost,
    host_verifications,
    host_has_profile_pic,
    host_identity_verified,
    host_listings_count,
    host_total_listings_count,
    calculated_host_listings_count,
	calculated_host_listings_count_entire_homes,
	calculated_host_listings_count_private_rooms,
	calculated_host_listings_count_shared_rooms,
	license,
    id,
    name,
    description,
    property_type,
    room_type,
    accommodates,
    bathrooms,
    bathrooms_text,
    bedrooms,
    beds,
    amenities,
    minimum_nights,
    maximum_nights,
    has_availability,
    instant_bookable,
    neighbourhood_cleansed,
    neighbourhood_group_cleansed,
    availability_30,
    availability_90,
    availability_365,
    number_of_reviews,
    review_scores_rating,
    review_scores_accuracy,
    review_scores_cleanliness,
    review_scores_checkin,
    review_scores_communication,
    review_scores_location,
    review_scores_value,
    price,
    quarter,
    year
FROM raw_q3_2024
UNION ALL
--getting data from raw_q4_2024 table
SELECT 
    host_id, 
    host_name,
    host_since,
    host_location,
    host_about,
    host_response_time,
    host_response_rate,
    host_acceptance_rate,
    host_is_superhost,
    host_verifications,
    host_has_profile_pic,
    host_identity_verified,
    host_listings_count,
    host_total_listings_count,
    calculated_host_listings_count,
	calculated_host_listings_count_entire_homes,
	calculated_host_listings_count_private_rooms,
	calculated_host_listings_count_shared_rooms,
	license,
    id,
    name,
    description,
    property_type,
    room_type,
    accommodates,
    bathrooms,
    bathrooms_text,
    bedrooms,
    beds,
    amenities,
    minimum_nights,
    maximum_nights,
    has_availability,
    instant_bookable,
    neighbourhood_cleansed,
    neighbourhood_group_cleansed,
    availability_30,
    availability_90,
    availability_365,
    number_of_reviews,
    review_scores_rating,
    review_scores_accuracy,
    review_scores_cleanliness,
    review_scores_checkin,
    review_scores_communication,
    review_scores_location,
    review_scores_value,
    price,
    quarter,
    year
FROM raw_q4_2024
UNION ALL
--getting data from raw_q1_2025 table
SELECT 
    host_id, 
    host_name,
    host_since,
    host_location,
    host_about,
    host_response_time,
    host_response_rate,
    host_acceptance_rate,
    host_is_superhost,
    host_verifications,
    host_has_profile_pic,
    host_identity_verified,
    host_listings_count,
    host_total_listings_count,
    calculated_host_listings_count,
	calculated_host_listings_count_entire_homes,
	calculated_host_listings_count_private_rooms,
	calculated_host_listings_count_shared_rooms,
	license,
    id,
    name,
    description,
    property_type,
    room_type,
    accommodates,
    bathrooms,
    bathrooms_text,
    bedrooms,
    beds,
    amenities,
    minimum_nights,
    maximum_nights,
    has_availability,
    instant_bookable,
    neighbourhood_cleansed,
    neighbourhood_group_cleansed,
    availability_30,
    availability_90,
    availability_365,
    number_of_reviews,
    review_scores_rating,
    review_scores_accuracy,
    review_scores_cleanliness,
    review_scores_checkin,
    review_scores_communication,
    review_scores_location,
    review_scores_value,
    price,
    quarter,
    year
FROM raw_q1_2025
UNION  ALL
--getting data from raw_q2_2025 table
SELECT 
    host_id, 
    host_name,
    host_since,
    host_location,
    host_about,
    host_response_time,
    host_response_rate,
    host_acceptance_rate,
    host_is_superhost,
    host_verifications,
    host_has_profile_pic,
    host_identity_verified,
    host_listings_count,
    host_total_listings_count,
    calculated_host_listings_count,
	calculated_host_listings_count_entire_homes,
	calculated_host_listings_count_private_rooms,
	calculated_host_listings_count_shared_rooms,
	license,
    id,
    name,
    description,
    property_type,
    room_type,
    accommodates,
    bathrooms,
    bathrooms_text,
    bedrooms,
    beds,
    amenities,
    minimum_nights,
    maximum_nights,
    has_availability,
    instant_bookable,
    neighbourhood_cleansed,
    neighbourhood_group_cleansed,
    availability_30,
    availability_90,
    availability_365,
    number_of_reviews,
    review_scores_rating,
    review_scores_accuracy,
    review_scores_cleanliness,
    review_scores_checkin,
    review_scores_communication,
    review_scores_location,
    review_scores_value,
    price,
    quarter,
    year
FROM raw_q2_2025
UNION  ALL
--getting data from raw_q3_2025 table
SELECT 
    host_id, 
    host_name,
    host_since,
    host_location,
    host_about,
    host_response_time,
    host_response_rate,
    host_acceptance_rate,
    host_is_superhost,
    host_verifications,
    host_has_profile_pic,
    host_identity_verified,
    host_listings_count,
    host_total_listings_count,
    calculated_host_listings_count,
	calculated_host_listings_count_entire_homes,
	calculated_host_listings_count_private_rooms,
	calculated_host_listings_count_shared_rooms,
	license,
    id,
    name,
    description,
    property_type,
    room_type,
    accommodates,
    bathrooms,
    bathrooms_text,
    bedrooms,
    beds,
    amenities,
    minimum_nights,
    maximum_nights,
    has_availability,
    instant_bookable,
    neighbourhood_cleansed,
    neighbourhood_group_cleansed,
    availability_30,
    availability_90,
    availability_365,
    number_of_reviews,
    review_scores_rating,
    review_scores_accuracy,
    review_scores_cleanliness,
    review_scores_checkin,
    review_scores_communication,
    review_scores_location,
    review_scores_value,
    price,
    quarter,
    year
FROM raw_q3_2025;

DROP TABLE IF EXISTS dim_hosts CASCADE;
--creating the dim_hosts table from the view
CREATE TABLE dim_hosts AS
SELECT DISTINCT ON (host_id)
    host_id,
    host_name,
    host_since,
    host_location,
    host_about,
    host_response_time,
    host_response_rate,
    host_acceptance_rate,
    CASE 
        WHEN host_is_superhost = 't' THEN TRUE
        WHEN host_is_superhost = 'f' THEN FALSE
        ELSE NULL
    END AS host_is_superhost,
    host_verifications,
    CASE 
        WHEN host_has_profile_pic = 't' THEN TRUE
        WHEN host_has_profile_pic = 'f' THEN FALSE
        ELSE NULL
    END AS host_has_profile_pic,
    CASE 
        WHEN host_identity_verified = 't' THEN TRUE
        WHEN host_identity_verified = 'f' THEN FALSE
        ELSE NULL
    END AS host_identity_verified,
    host_listings_count,
    host_total_listings_count,
    calculated_host_listings_count,
	calculated_host_listings_count_entire_homes,
	calculated_host_listings_count_private_rooms,
	calculated_host_listings_count_shared_rooms,
	license
FROM all_raw_listings_view
ORDER BY host_id, year DESC, quarter DESC;
--adding primary key to dim_hosts table
ALTER TABLE dim_hosts
ADD PRIMARY KEY (host_id);

DROP TABLE IF EXISTS dim_listings CASCADE;
--creating the dim_listings table from the view
CREATE TABLE dim_listings AS
SELECT DISTINCT ON (id)
    id,
    name,
    description,
    property_type,
    room_type,
    accommodates,
    bathrooms,
    bathrooms_text AS bathrooms_description,
    bedrooms,
    beds,
    amenities,
    minimum_nights,
    maximum_nights,
    CASE 
        WHEN has_availability = 't' THEN TRUE
        WHEN has_availability = 'f' THEN FALSE
        ELSE NULL
    END AS has_availability,
    CASE 
        WHEN instant_bookable = 't' THEN TRUE
        WHEN instant_bookable = 'f' THEN FALSE
        ELSE NULL
    END AS instant_bookable,
    neighbourhood_cleansed AS neighbourhood,
    neighbourhood_group_cleansed AS district,
    availability_30,
    availability_90,
    availability_365,
    number_of_reviews,
    review_scores_rating,
    review_scores_accuracy,
    review_scores_cleanliness,
    review_scores_checkin,
    review_scores_communication,
    review_scores_location,
    review_scores_value,
    host_id
FROM all_raw_listings_view
WHERE neighbourhood_cleansed IS NOT NULL
AND host_id IS NOT NULL
AND accommodates IS NOT NULL
ORDER BY id, year DESC, quarter DESC;
--adding primary key and foreign key to dim_listings table
ALTER TABLE dim_listings
ADD PRIMARY KEY (id),
ADD FOREIGN KEY (host_id) REFERENCES dim_hosts(host_id);

DROP TABLE IF EXISTS fact_listings CASCADE;
--creating the fact_listings table from the view
CREATE TABLE fact_listings AS
SELECT
    id AS listings_id,
    REPLACE(quarter, 'Q', '')::INTEGER AS quarter,
    year::INTEGER,
    REPLACE(REPLACE(price, '$', ''), ',', '')::NUMERIC AS price
FROM all_raw_listings_view
WHERE price IS NOT NULL
AND neighbourhood_cleansed IS NOT NULL
AND host_id IS NOT NULL
AND accommodates IS NOT NULL
AND REPLACE(REPLACE(price, '$', ''), ',', '')::NUMERIC > 0;
--adding primary keys and foreign key to fact_listings table
ALTER TABLE fact_listings
ADD PRIMARY KEY (listings_id, quarter, year),
ADD FOREIGN KEY (listings_id) REFERENCES dim_listings(id);