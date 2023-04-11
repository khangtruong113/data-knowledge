package main.functional

object MapFlatMapFilter {
  val list = List(1, 2, 3)

  println(list.head)
  println(list.tail)

  //map
  print(list.map(_ + 1))

  //filter
  println(list.filter(_ % 2 == 0))

  //flatmap
  val toPair = (x: Int) => List(x, x+1)
  println(list.flatMap(toPair))

  //print all combination between 2 lists
  val number = List(1,2,3,4)
  val chars = List('a', 'b', 'c', 'd')
  val colour= List("black", "white")
  //list "a1", "a2",...
  //solution
  val combination = number.flatMap(n => chars.map(c=> ""+ c + n))
  println(combination)

  //'iterating method'

  //foreach
  list.foreach(println)

  //for-comprehension
  val forCombination = for {
    n <- number if n%2 == 0
    c <- chars
    colour <- colour
  } yield "" + c + n + "-" + colour
  println(forCombination)

  for {
    n <- number
  }
    println(n)

  list.map {
    x => x*2
  }
}
