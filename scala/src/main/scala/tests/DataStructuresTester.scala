package tests

import data_structures._

class DataStructuresTester {
  val startTestingMessage: String =
      "------------Starting Testing-------------"
  val completeTestingMessage: String =
      "------------Testing Complete-------------"

  def getOptions(): String = {
    "\n1: Singly Linked List\n" +
    "2: Doubly Linked list\n" +
    "q: Quit"
  }

  def testSinglyLinkedList(): Unit = {
    println(startTestingMessage)
    println("Creating list with data 1...")
    var list: SinglyLinkedList = new SinglyLinkedList(new SingleNode(1))
    println(list)
    println("Adding some elements...")
    list.add(2); list.add(3); list.add(4); list.add(5);
    println(list)
    println("Mapping x = x * 2...")
    list = list.map((x) => x match {
      case num: Int => num * 2
      case _ => x
    })
    println(list)
    println("Swapping out some elements...")
    list.getHead().getNext().getNext().setNext(new SingleNode(7))
    println(list)
    println("Use fold right to add...")
    println(list.foldRight((x: Int, y) => y match {
      case num: Int => x + num
      case _ => x
    }, 0))
    println(completeTestingMessage)
  }

  def testDoublyLinkedList(): Unit = {
    println(startTestingMessage)
    println("Creating list with 0 node...")
    var list: DoublyLinkedList = new DoublyLinkedList(new DoubleNode(0))
    println(list)
    println("Adding two to the front...")
    list.addToTail(1); list.addToTail(2)
    println(list)
    println("Adding two to the back...")
    list.addToHead(-1); list.addToHead(-2)
    println(list)
    println("Map x => x * -2 to list...")
    list = list.map(x => x match {
      case x: Int => x * -2
      case _ => x
    })
    println(list)
    println(completeTestingMessage)
  }

  def runTests(): Unit = {
    var running = true
    while (running) {
      println(getOptions())
      val in: String = readLine()
      in match {
        case "1" => testSinglyLinkedList()
        case "2" => testDoublyLinkedList()
        case "q" => running = false
        case _ => "Invalid input"
      }
    }
  }
}
