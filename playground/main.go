package main

import (
	"fmt"
	"strconv"
	"time"
)

const (
	numOfUrls   = 10000
	numOfWorker = 5
)

func crawUrl(queue <-chan int, workerId string) {
	for v := range queue {
		fmt.Printf("Worker %s is crawling URL %d\n", workerId, v)
		time.Sleep(1 * time.Second)
	}
}

func startQueue() <-chan int {
	queue := make(chan int, 100)
	go func() {
		defer close(queue)

		for i := 0; i < numOfUrls; i++ {
			queue <- i
			fmt.Printf("URL %d has been enqueued\n", i)
		}
	}()

	return queue
}

func main() {
	queue := startQueue()

	for i := 0; i < numOfWorker; i++ {
		go crawUrl(queue, strconv.Itoa(i))
	}

	time.Sleep(5 * time.Minute)
}
