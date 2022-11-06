## batch processing
*ad hoc / scheduled processing*
- a lot of data is collected before a batch is done


## stream processing
*real time processing*
- batch relies on collected data, while stream processing relies on **continuous** data

## when to use batch processing
- End of day feeds - apache spark, apache hadoop. These frameworks parse files, process them and transform them how you'd like to be stored in a database (using mapreduce?)

### when to use stream processing
- trying to put different pieces of information into a kafka topic (?)
- multiple applications which are publishing different types of metrics
- in order to get real time information, you need to process data in real time

**you need to choose between batch and stream processing whenever you need to process some kind of data - overall, batch is better if you do not need data to be processed quickly, and it is acceptable to process it at the end of the day**
