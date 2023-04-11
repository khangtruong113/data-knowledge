package main.functional

import scala.util.Random

object Sequences extends App {
  //Seq
  //general interface for data structures that
  //- have a well defined order
  //- can be indexed
  // support many operations :
  //+ apply, interator, length, reverse for indexing and iterating
  val aSequence = Seq(1, 2, 3, 4)
  println(aSequence)
  println(aSequence.reverse)
  println(aSequence(2))
  println(aSequence ++ Seq(8, 6, 7))
  println(aSequence.sorted)

  //ranges
  val aRange: Seq[Int] = 1 to 10
  aRange.foreach(println)

  // do it as
  (1 to 10).foreach(x => println("hello"))

  //lists
  val aList = List(1, 2, 3)
  val prepend = 42 :: aList
  println(prepend)

  val prepending = 42 +: aList :+ 89 //append 42 and prepend 89

  val apples5 = List.fill(5)("apple") //construct a list with 5 times of apple

  println(aList.mkString("-")) //concatinate and put the character between them

  //arrays
  //quite same to java arrays
  //array are mutable
  //array indexing is fast

  val numbers = Array(1,2,3,4)
  val threeElements = Array.ofDim[Int](3)
  threeElements.foreach(println)
  //they have 3 default value of this array.

  //mutation
  numbers(2) = 0 //syntax sugar for numbers.update(2,0)
  println(numbers.mkString(" "))

  //array and seq
  val numbersSeq: Seq[Int] = numbers

  print(numbersSeq) // the type is WrappedArray , they are implicit conversion

  //VECTOR:
//  default implementation for immutable sequences
//effectively constant indexed read and write
// fast element addition: append/prepend
//implemented as a fixed -branched trie
// good performance for very large size
val vector: Vector[Int] = Vector(1,2,3)
  

}

