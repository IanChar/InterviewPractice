package main

import tests._

object Main {

  def getOptions(): String = {
    "\n1: Data Structures\n" +
    "q: Quit"
  }

  def main(args: Array[String]): Unit = {
    var running = true
    val dsTester: DataStructuresTester = new DataStructuresTester()
    while (running) {
      println(getOptions())
      val in: String = readLine()
      in match {
        case "1" => dsTester.runTests()
        case "q" => running = false
        case _ => "Invalid Input"
      }
    }
  }
}
