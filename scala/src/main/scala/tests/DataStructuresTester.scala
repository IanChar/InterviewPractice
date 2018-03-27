package tests

import data_structures._

class DataStructuresTester {
  val startTestingMessage: String =
      "------------Starting Testing-------------"
  val completeTestingMessage: String =
      "------------Testing Complete-------------"

  def isCorrect(received: Any, expected: Any): Boolean = {
    if (received == expected) {
      println(received + " matches " + expected)
      return true
    } else {
      println(received + " did not match " + expected)
      return false
    }
  }

  def getOptions(): String = {
    "\n-------------DATA STRUCTURES------------\n" +
    "1: Singly Linked List\n" +
    "2: Doubly Linked list\n" +
    "3: Binary Tree\n" +
    "q: Quit\n" +
    "-----------------------------------------"
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

  def testBinaryTree(): Unit = {
    var correct: Int = 0
    println(startTestingMessage)

    println("Creating binary tree...")
    var bTree: BinaryTree = new BinaryTree(new TreeNode(1))
    var curr: TreeNode = bTree.getRoot()
    curr.setLeft(new TreeNode(2))
    curr.setRight(new TreeNode(3))
    curr = curr.getLeft().get
    curr.setLeft(new TreeNode(4))
    curr.setRight(new TreeNode(5))

    println("Pre order traversal:")
    if (isCorrect(bTree.preorder(), "1, 2, 4, 5, 3")) {
      correct += 1
    }
    println("In order traversal:")
    if (isCorrect(bTree.inorder(), "4, 2, 5, 1, 3")) {
      correct += 1
    }
    println("Post order traversal:")
    if (isCorrect(bTree.postorder(), "4, 5, 2, 3, 1")) {
      correct += 1
    }
    println(correct + "/3 Tests Passed")
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
        case "3" => testBinaryTree()
        case "q" => running = false
        case _ => "Invalid input"
      }
    }
  }
}
