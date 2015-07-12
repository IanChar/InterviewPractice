object DataStructuresTester {
  val startTestingMessage: String =
      "------------Starting Testing-------------"
  val completeTestingMessage: String =
      "------------Testing Complete-------------"

  def getOptions(): String = {
    "\n1: Singly Linked List\n" +
    "q: Quit"
  }

  def testSinglyLinkedList(): Unit = {
    println(startTestingMessage)
    println("Creating list with data 1...")
    val list: SinglyLinkedList = new SinglyLinkedList(1)
    println(list)
    println("Adding some elements...")
    list.add(2); list.add(3); list.add(4); list.add(5);
    println(list)
    println("Swapping out some elements...")
    list.getHead().getNext().getNext().setNext(new Node(76))
    println(list)
    println(completeTestingMessage)
  }

  def main(args: Array[String]): Unit = {
    var running = true
    while (running) {
      println(getOptions())
      val in: String = readLine()
      in match {
        case "1" => testSinglyLinkedList()
        case "q" => running = false
        case _ => "Invalid input"
      }
    }
  }
}
