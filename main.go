package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
)

func main() {
	scriptPath := "./main.sh"

	cmd := exec.Command("bash", scriptPath)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Script execution completed.")
}
