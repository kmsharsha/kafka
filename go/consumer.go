package main

import (
     "fmt"
     "gopkg.in/confluentinc/confluent-kafka-go.v1/kafka"
)

func main() {
        conn, err := kafka.NewConsumer(&kafka.ConfigMap{
                     "bootstrap.servers": "localhost",
                     "group.id": "go_id_1",
                     "auto.offset.reset": "earliest",
                 })

     if err != nil {
         panic(err)
     }

     conn.SubscribeTopics([]string{"mytopic"}, nil)

     for {
         msg, err := conn.ReadMessage(-1)
         if err == nil {
             fmt.Printf("Message on %s: %s\n", msg.TopicPartition, string(msg.Value))
         } else {
             fmt.Printf("Consumer error: %v (%v)\n", err, msg)
         }
     }
     conn.Close()
}
