package data_structures

case class DoubleNode(var data: Any, var prev: DoubleNode, var next: DoubleNode)
    extends Node {

  def this(data: Any) = this(data, null, null)
  def this(data: Any, prev: DoubleNode) = this(data, prev, null)

  override def get(): Any = data
  override def set(newData: Any): Unit = {data = newData}

  def setPrevious(previous: Any): Unit = previous match {
    case previous: DoubleNode => {
      prev = previous
      prev.next = this
    }
    case _ => prev = new DoubleNode(previous, null, this)
  }

  def getPrevious(): DoubleNode = prev

  def setNext(nxt: Any): Unit = nxt match {
    case nxt: DoubleNode=> {
      next = nxt
      nxt.prev = this
    }
    case _ => next = new DoubleNode(nxt, this, null)
  }

  def getNext(): DoubleNode = next

  override def toString(): String = data.toString()
}

class DoublyLinkedList(private var head: DoubleNode) {
  private var tail: DoubleNode = head

  def this() = this(null)

  def getHead(): DoubleNode = head
  def setHead(h: DoubleNode): Unit = {head = h}
  def getTail(): DoubleNode = tail
  def setTail(t: DoubleNode): Unit = {tail = t}

  def addToTail(data: Any): Unit = {
    if (head == null) {
      data match {
        case node: DoubleNode => head = node
        case _ => head = new DoubleNode(data)
      }
      tail = head
    } else {
      tail.setNext(data)
      tail = tail.getNext()
    }
  }

  def addToHead(data: Any): Unit = {
    if (head == null) {
      data match {
        case node: DoubleNode => head = node
        case _ => head = new DoubleNode(data)
      }
      tail = head
    } else {
      head.setPrevious(data)
      head = head.getPrevious()
    }
  }

  def map(f: Any => Any): DoublyLinkedList = {
    def mapCurr(curr: DoubleNode, f: Any => Any,
        acc: DoublyLinkedList): DoublyLinkedList = curr match {
      case DoubleNode(d, p, n: DoubleNode) => {
        acc.addToTail(f(d))
        mapCurr(n, f, acc)
      }
      case DoubleNode(d, p, _) => {
        acc.addToTail(f(d))
        acc
      }
    }

    mapCurr(head, f, new DoublyLinkedList())
  }

  override def toString(): String = {
    def printCurr(curr: DoubleNode, acc: String): String = curr match {
      case DoubleNode(d, p, n) => n match {
        case node: DoubleNode => printCurr(node, acc + d + " <-> ")
        case _ => acc + d
      }
      case _ => ""
    }
    "[" + printCurr(head, "") + "]"
  }
}
