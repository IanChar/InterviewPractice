case class SingleNode(var data: Any, var next: SingleNode)
    extends Node {
  def this(data: Any) = this(data, null)
  def this(data: Any, nextData: Any) = this(data, new SingleNode(nextData))

  override def get(): Any = data
  override def set(newData: Any): Unit = {data = newData}

  def setNext(next: Any): Unit = {
    next match {
      case node: SingleNode => this.next = node
      case _ => this.next = SingleNode(next, null)
    }
  }

  def getNext(): SingleNode = {
    next
  }

  override def toString(): String = data.toString()
}

class SinglyLinkedList(private var head: SingleNode) {
  private var last: SingleNode = head

  def this() = this(null)

  def getHead(): SingleNode = {
    head
  }

  def add(data: Any): Unit = {
    if (last == null) {
      data match {
        case node: SingleNode => head = node
        case _ => head = new SingleNode(data)
      }
      last = head
    } else {
      last.setNext(new SingleNode(data))
      last = last.getNext()
    }
  }

  def map(f: Any => Any): SinglyLinkedList = {
    def mapCurr(curr: SingleNode, f: Any => Any,
        acc: SinglyLinkedList): SinglyLinkedList = curr match {
      case SingleNode(d, n: SingleNode) => {
        acc.add(f(d))
        mapCurr(n, f, acc)
      }
      case SingleNode(d, _) => {
        acc.add(f(d))
        acc
      }
    }
    mapCurr(head, f, new SinglyLinkedList())
  }

  def foldRight[T](f: (T, Any) => T, acc: T): T = {
    def foldCurr(curr: SingleNode, f: (T, Any) => T,
        acc: T): T = curr match {
      case SingleNode(d, n: SingleNode) => {
        foldCurr(n, f, f(acc, d))
      }
      case SingleNode(d, _) => {
        f(acc, d)
      }
    }
    foldCurr(head, f, acc)
  }

  override def toString(): String = {
    def printCurrNode(curr: SingleNode, acc: String): String = curr match {
      case SingleNode(d, n) => n match {
        case node: SingleNode => printCurrNode(node, acc + d + " -> ")
        case _ => acc + curr
      }
      case _ => ""
    }
    "[" + printCurrNode(head, "") + "]"
  }
}
