CREATE TABLE "dropoff_location_dim"(
    "dropoff_location_id" BIGINT NOT NULL,
    "dropoff_latitude" DOUBLE PRECISION NOT NULL,
    "dropoff_longitude" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "dropoff_location_dim" ADD PRIMARY KEY("dropoff_location_id");
CREATE TABLE "fact_table"(
    "trip_id" BIGINT NOT NULL,
    "VendorID" INTEGER NOT NULL,
    "datetime_id" BIGINT NOT NULL,
    "passenger_count_id" BIGINT NOT NULL,
    "trip_distance_id" BIGINT NOT NULL,
    "rate_code_id" BIGINT NOT NULL,
    "store_and_fwd_flag" BOOLEAN NOT NULL,
    "pickup_location_id" BIGINT NOT NULL,
    "dropoff_location_id" BIGINT NOT NULL,
    "payment_type_id" BIGINT NOT NULL,
    "fare_amount" DOUBLE PRECISION NOT NULL,
    "extra" DOUBLE PRECISION NOT NULL,
    "mta_tax" DOUBLE PRECISION NOT NULL,
    "tip_amount" DOUBLE PRECISION NOT NULL,
    "tolls_amount" DOUBLE PRECISION NOT NULL,
    "improvement_surcharge" DOUBLE PRECISION NOT NULL,
    "total_amount" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "fact_table" ADD PRIMARY KEY("trip_id");
CREATE TABLE "pickup_location_dim"(
    "pickup_location_id" BIGINT NOT NULL,
    "pickup_latitude" DOUBLE PRECISION NOT NULL,
    "pickup_longitude" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "pickup_location_dim" ADD PRIMARY KEY("pickup_location_id");
CREATE TABLE "passenger_count_dim"(
    "passenger_count_id" BIGINT NOT NULL,
    "passenger_count" INTEGER NOT NULL
);
ALTER TABLE
    "passenger_count_dim" ADD PRIMARY KEY("passenger_count_id");
CREATE TABLE "trip_distance_dim"(
    "trip_distance_id" BIGINT NOT NULL,
    "trip_distance" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "trip_distance_dim" ADD PRIMARY KEY("trip_distance_id");
CREATE TABLE "payment_type_dim"(
    "payment_type_id" BIGINT NOT NULL,
    "payment_type" INTEGER NOT NULL,
    "payment_type_name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "payment_type_dim" ADD PRIMARY KEY("payment_type_id");
CREATE TABLE "datetime_dim"(
    "datetime_id" BIGINT NOT NULL,
    "tpep_pickup_datetime" DATE NOT NULL,
    "pick_hour" INTEGER NOT NULL,
    "pick_day" INTEGER NOT NULL,
    "pick_month" INTEGER NOT NULL,
    "pick_year" INTEGER NOT NULL,
    "pick_weekday" BOOLEAN NOT NULL,
    "tpep_dropoff_datetime" DATE NOT NULL,
    "drop_hour" INTEGER NOT NULL,
    "drop_day" INTEGER NOT NULL,
    "drop_month" INTEGER NOT NULL,
    "drop_weekday" BOOLEAN NOT NULL
);
ALTER TABLE
    "datetime_dim" ADD PRIMARY KEY("datetime_id");
CREATE TABLE "rate_code_dim"(
    "rate_code_id" BIGINT NOT NULL,
    "RatecodeID" INTEGER NOT NULL,
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