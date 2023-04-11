package main.functional

import scala.util.Random

object Options extends App {
  //an option is a wrapper for a value that might be present or not

  // some wraps a concrete value | none is a singleton for absent values

  //  for eg, find the wrong key for a map

  val myFirstOption: Option[Int] = Some(4)
  val noOption: Option[Int] = None

  //option is design for unsafe API or unsafe method

  def unsafeMethod(): String = null

  val result = Some(unsafeMethod()) // wrong since you miught get some(null), some must have a value inside
  val result2 = Option(unsafeMethod())
  print(result2) // -> None

  //we should let Option to check the result for us instead of do it ourselves

  def backupMethod(): String = "a valid result"
  val chainedResult = Option(unsafeMethod()).orElse(Option(backupMethod()))

  //DESIGN unsafe API
  def  betterUnsafeMethod(): Option[String] = None
  def  betterBackupMethod(): Option[String] = Some("A valid result")

  val betterChainResult = betterUnsafeMethod() orElse betterBackupMethod()

  //functions on Options
  print(myFirstOption.isEmpty) // -> false
  println(myFirstOption.get) // unsafe if the option is safe

  //map, flatmap and filter
  println(myFirstOption.map(_ * 2))
  println(myFirstOption.filter(x => x > 10)) //return none since 4 is < than 10
  println(myFirstOption.flatMap(x => Option(x*10))) //return 40

  //for comprehension

  /*
  exercise

  */

  val config: Map[String, String] = Map{
    //fetched from else where
    "host" -> "176.45.36.1"
    "port" -> "80"
  }

  class Connection{
    def connect = "connect" //connect to some server
  }

  object Connection {
    val random = new Random(System.nanoTime())
    def apply(host: String, port: String): Option[Connection] =
      if(random.nextBoolean()) Some(new Connection)
      else None
  }

  /*
  explanation
  if ( h != null)
    if(p != null)
      return connection.apply(h,p)
  */
  // estalish a connection, if so- print the connect method
  val host = config.get("host")
  val port = config.get("port")

  val connection = host.flatMap(h => port.flatMap(p => Connection.apply(h, p)))
  /*
  * if(c!= null )
  *   return c.connect
  * return null
  * */
  val connectionStatus = connection.map(c => c.connect)

  connectionStatus.foreach(println)

  config.get("host").flatMap(host => config.get("port").
    flatMap(port => Connection(host, port).
      map(connection => connection.connect)))

  //for-comprehension
  val connectionStatusFor = for {
    host <- config.get("host")
    port <- config.get("port")
    connection <- Connection(host, port)
  } yield connection.connect

  connectionStatusFor.foreach(println)

  //remember when you working with something might be null -> use option
}
