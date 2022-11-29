import twint
import nest_asyncio
nest_asyncio.apply()

#configure
c= twint.Config()
c.Search = "covid"


#run
twint.run.Search(c)


