require('dotenv').config();
const express = require("express");
const kafka = require("kafka-node");
const {KafkaClient, Consumer} = kafka;
const app = express();
const port = process.env.KAFKA_HOST || 'localhost:9092';

const client = new KafkaClient({kafkaHost: "localhost:9092"});
const consumer = new Consumer(
    client,
    [{topic: "task-events", partition: 0}],
    {
        autoCommit: true,
    }
);

consumer.on("message", (message) => {
    console.log("Received task event:", message.value);
});

consumer.on("error", (err) => {
    console.error("Error in kafka consumer:", err);
});

app.get("/", (req, res) => {
    res.send("Notification Service is running");
});

app.listen(port, () => {
    console.log(`Notification Service is running at http://localhost:${port}`);
});

