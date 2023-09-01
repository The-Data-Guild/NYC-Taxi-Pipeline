CREATE TABLE "dropoff_location_dim"(
    "dropoff_location_id" BIGINT NOT NULL,
    "dropoff_latitude" BIGINT NOT NULL,
    "dropoff_longitude" BIGINT NOT NULL
);
ALTER TABLE
    "dropoff_location_dim" ADD PRIMARY KEY("dropoff_location_id");
CREATE TABLE "fact_table"(
    "trip_id" BIGINT NOT NULL,
    "VendorID" BIGINT NOT NULL,
    "datetime_id" BIGINT NOT NULL,
    "passenger_count_id" BIGINT NOT NULL,
    "trip_distance_id" BIGINT NOT NULL,
    "rate_code_id" BIGINT NOT NULL,
    "store_and_fwd_flag" BIGINT NOT NULL,
    "pickup_location_id" BIGINT NOT NULL,
    "dropoff_location_id" BIGINT NOT NULL,
    "payment_type_id" BIGINT NOT NULL,
    "fare_amount" BIGINT NOT NULL,
    "extra" BIGINT NOT NULL,
    "mta_tax" BIGINT NOT NULL,
    "tip_amount" BIGINT NOT NULL,
    "tolls_amount" BIGINT NOT NULL,
    "improvement_surcharge" BIGINT NOT NULL,
    "total_amount" BIGINT NOT NULL
);
ALTER TABLE
    "fact_table" ADD PRIMARY KEY("trip_id");
CREATE TABLE "pickup_location_dim"(
    "pickup_location_id" BIGINT NOT NULL,
    "pickup_latitude" BIGINT NOT NULL,
    "pickup_longitude" BIGINT NOT NULL
);
ALTER TABLE
    "pickup_location_dim" ADD PRIMARY KEY("pickup_location_id");
CREATE TABLE "passenger_count_dim"(
    "passenger_count_id" BIGINT NOT NULL,
    "passenger_count" BIGINT NOT NULL
);
ALTER TABLE
    "passenger_count_dim" ADD PRIMARY KEY("passenger_count_id");
CREATE TABLE "trip_distance_dim"(
    "trip_distance_id" BIGINT NOT NULL,
    "trip_distance" BIGINT NOT NULL
);
ALTER TABLE
    "trip_distance_dim" ADD PRIMARY KEY("trip_distance_id");
CREATE TABLE "payment_type_dim"(
    "payment_type_id" BIGINT NOT NULL,
    "payment_type" BIGINT NOT NULL,
    "payment_type_name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "payment_type_dim" ADD PRIMARY KEY("payment_type_id");
CREATE TABLE "datetime_dim"(
    "datetime_id" BIGINT NOT NULL,
    "tpep_pickup_datetime" BIGINT NOT NULL,
    "pick_hour" BIGINT NOT NULL,
    "pick_day" BIGINT NOT NULL,
    "pick_month" BIGINT NOT NULL,
    "pick_year" BIGINT NOT NULL,
    "pick_weekday" BIGINT NOT NULL,
    "tpep_dropoff_datetime" BIGINT NOT NULL,
    "drop_hour" BIGINT NOT NULL,
    "drop_day" BIGINT NOT NULL,
    "drop_month" BIGINT NOT NULL,
    "drop_weekday" BIGINT NOT NULL
);
ALTER TABLE
    "datetime_dim" ADD PRIMARY KEY("datetime_id");
CREATE TABLE "rate_code_dim"(
    "rate_code_id" BIGINT NOT NULL,
    "RatecodeID" BIGINT NOT NULL,
    "rate_code_name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "rate_code_dim" ADD PRIMARY KEY("rate_code_id");
ALTER TABLE
    "fact_table" ADD CONSTRAINT "fact_table_pickup_location_id_foreign" FOREIGN KEY("pickup_location_id") REFERENCES "pickup_location_dim"("pickup_location_id");
ALTER TABLE
    "fact_table" ADD CONSTRAINT "fact_table_passenger_count_id_foreign" FOREIGN KEY("passenger_count_id") REFERENCES "passenger_count_dim"("passenger_count_id");
ALTER TABLE
    "fact_table" ADD CONSTRAINT "fact_table_trip_distance_id_foreign" FOREIGN KEY("trip_distance_id") REFERENCES "trip_distance_dim"("trip_distance_id");
ALTER TABLE
    "fact_table" ADD CONSTRAINT "fact_table_payment_type_id_foreign" FOREIGN KEY("payment_type_id") REFERENCES "payment_type_dim"("payment_type_id");
ALTER TABLE
    "fact_table" ADD CONSTRAINT "fact_table_dropoff_location_id_foreign" FOREIGN KEY("dropoff_location_id") REFERENCES "dropoff_location_dim"("dropoff_location_id");
ALTER TABLE
    "fact_table" ADD CONSTRAINT "fact_table_rate_code_id_foreign" FOREIGN KEY("rate_code_id") REFERENCES "rate_code_dim"("rate_code_id");
ALTER TABLE
    "fact_table" ADD CONSTRAINT "fact_table_datetime_id_foreign" FOREIGN KEY("datetime_id") REFERENCES "datetime_dim"("datetime_id");