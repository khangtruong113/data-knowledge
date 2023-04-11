package main.functional

object AnonymousFunctions extends App {

  val doubler = new Function[Int, Int]{
    override def apply(x: Int): Int = x * 2
  }
  //this way too object oriented

  //functional way
  val doubler2 = (x: Int) => x * 2 // an instance of function1

  //this is anomyous function ( LAMBDA )
  val doubler3: Int => Int = x => x * 2
  // compiler will understand the first x as Int, the second will match the second Int after the =>

  //multiple params in a lambda
  val adder: (Int, Int) => Int =  (a: Int, b: Int)=> a + b

  //with no params
  val justDoSomething: () => Int = () => 3

  println(justDoSomething)
  println(justDoSomething()) //the actual call

  //when it comes to lambda we need to call them with ()

  //curly braces with Lambda
  val stringToInt = { (str:String) =>
    str.toInt
  }

  //MORE syntactic sugar
  val niceIncrementer: Int => Int = _ + 1 // this is the same to x => x + 1
  val niceAdder: (Int, Int) => Int = _ + _ //where each underscore a parameter which is equals to : (a,b) => a + b


  val supAdd = (x: Int)=> (y: Int) => x + y
  println(supAdd(3)(4 ))
}
