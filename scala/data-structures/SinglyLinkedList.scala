class Node(_data: Any) {
   private var data = _data
   private var next:Node = null

   def get() = {
     data
   }

   def set(newData: Any) = {
     data = newData
   }

   def setNext(next:Node) = {
     this.next = next
   }

   def getNext():Node = {
     next
   }

   override def toString(): String = get().toString()
 }

class SinglyLinkedList(_head: Node) {
  private val head: Node = _head

  def this(data: Any) = {
    this(new Node(data))
  }

  def getHead(): Node = {
    head
  }

  override def toString(): String = {
    def printCurrNode(curr: Node, acc: String): String = curr.getNext() match {
      case nxt: Node => printCurrNode(nxt, acc + curr + " -> ")
      case _ => acc + curr
    }
    "[" + printCurrNode(head, "") + "]"
  }
}
