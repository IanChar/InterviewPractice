object DataStructuresTester {
  def getOptions(): String = {
    "1: Singly Linked List"
  }

  def main(args: Array[String]): Unit = {
    println(getOptions())
    val in: String = readLine()
    println("You put in" + in)
  }
}
