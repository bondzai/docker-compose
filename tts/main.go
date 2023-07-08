package main

import (
	"fmt"
	"log"

	"github.com/lorniu/go-ttsbot"
)

func main() {
	client := ttsbot.NewClient()

	// Set TTS options
	options := &ttsbot.Options{
		Text:      "Hello, world!",
		Lang:      "en-US",
		Speed:     1.0,
		Volume:    1.0,
		OutputDir: "./output",
	}

	// Generate TTS audio file
	filePath, err := client.Generate(options)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("TTS audio file generated: %s\n", filePath)
}
