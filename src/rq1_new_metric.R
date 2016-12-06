cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

all_needed_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_needed_content.csv"
all_posts_data <- read.csv(all_needed_file)

topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/with_title_all_corpus_20_topics/20_TopicProb.csv"
topic_prob_data <- read.csv(topic_prob_file)

topic_names <- colnames(topic_prob_data, do.NULL = TRUE, prefix = "col")
doc_names <- rownames(topic_prob_data, do.NULL = TRUE, prefix = "row")

topic_names <- topic_names[!topic_names %in% "X"]
#print(topic_names)
#print(doc_names)
len_doc_names <- length(doc_names)
len_top_names <- length(topic_names)
dic_topics <- vector(mode="list", length=len_doc_names)
names(dic_topics) <- doc_names
###threshold 
topic_prob_cutoff <- 0.10
for(doc_ind in 2:len_doc_names)
{
  
  topics_for_this_doc <- vector(mode="numeric", length=len_top_names+1)
  dom_topic_for_this_doc <- rep(0, len_top_names+1)
  for(topic_ind in 1:len_top_names+1)
  {
    topic_prob_for_doc <- topic_prob_data[doc_ind, topic_ind]
    topics_for_this_doc[topic_ind] <- topic_prob_for_doc
  }
  #max_topic_prob <-  max(topics_for_this_doc)
  #print(max_topic_prob)
  index_with_max_prob <- which(topics_for_this_doc >= topic_prob_cutoff)
  #print("-----")
  #print(index_with_max_prob)
  dom_topic_for_this_doc[index_with_max_prob] <- 1
  #print(dom_topic_for_this_doc)
  dic_topics[[doc_ind]] <- dom_topic_for_this_doc
  #print("-----")  
}
#print(dic_topics)
len_dic_topic <- length(dic_topics)
for(top_inex in 1:len_top_names+1)
{
  print("#########################")
  print(top_inex)
  print("---------------")
  qaa_for_topic <- 0 
  qnaa_for_topic <- 0   
  qaa_vector <- vector(mode="numeric", length=len_dic_topic)
  qnaa_vector <- vector(mode="numeric", length=len_dic_topic)  
  print("Total IaC-related questions")
  print(len_dic_topic)
  len_dic_topic <- 105660
  print("---------------")  
  for(doc_index in 2:len_dic_topic)
  {
    tmp_ <-  dic_topics[[doc_index]][top_inex]
    if(tmp_==1)
    {
      #print("*****")
      #print("The question is:")
      #print(doc_index)
      matched_row_accepted_ans_id <- all_posts_data[doc_index, 3]
      #print(matched_row_accepted_ans_id)
      if(length(matched_row_accepted_ans_id) > 0)
      {
        qaa_for_topic <- qaa_for_topic + 1
        qaa_vector <- c(qaa_vector, matched_row_accepted_ans_id)
      }
#       else
#       {
#         qnaa_for_topic <- qnaa_for_topic + 1        
#         qnaa_vector <- c(qnaa_vector, matched_row_accepted_ans_id)        
#       }
      #print("*****")
    }
    #print(tmp_)
    #nddt_for_this_topic[doc_index] <-  tmp_
  }

  print("***QAA***")
  print(qaa_for_topic)
  #qaa_vector <- qaa_vector[!qaa_vector %in% c(0)]
  #print(length(qaa_vector))
  print("***QNAA***")
  qnaa_for_topic <- len_dic_topic - qaa_for_topic
  print(qnaa_for_topic)
  #qnaa_vector <- qnaa_vector[!qnaa_vector %in% c(0)]
  #print(length(qnaa_vector))
  comm_confidence <- qaa_for_topic  / len_dic_topic 
  comm_confusion  <- qnaa_for_topic / len_dic_topic 
  print("***Community confidence***")
  print(comm_confidence)
  print("***Community confusion***")
  print(comm_confusion)
  print("#########################")
}


t2 <- Sys.time()
print(t2 - t1)  # 

rm(list = setdiff(ls(), lsf.str()))