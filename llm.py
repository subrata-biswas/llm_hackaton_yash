#%env OPENAI_API_KEY=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

import os
    
from llama_index.core import (
        SimpleDirectoryReader,
        VectorStoreIndex,
        StorageContext,
        load_index_from_storage,
    )
from llama_index.core.tools import QueryEngineTool, ToolMetadata

from pymilvus import connections
from llama_index.vector_stores.milvus import MilvusVectorStore

from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI


def llm(prompt):
    
    try:
        storage_context = StorageContext.from_defaults(
            persist_dir="./storage/med"
        )
        med_index = load_index_from_storage(storage_context)
    
        index_loaded = True
    except:
        index_loaded = False
    
    
    ref_files = os.listdir("/Users/home/Documents/Projects/Made/llm_hackaton_yash/data/10k/Health_PDF/")
    ref_files = ["/Users/home/Documents/Projects/Made/llm_hackaton_yash/data/10k/Health_PDF/" + f for f in ref_files if f.endswith('.pdf')]
    ref_files


    if not index_loaded:
        med_docs = SimpleDirectoryReader(
            input_files=ref_files
        ).load_data()
    
        # build index
        vector_store_med = MilvusVectorStore(dim=1536, collection_name="med", overwrite=True)
        storage_context_med = StorageContext.from_defaults(vector_store=vector_store_med)
        med_index = VectorStoreIndex.from_documents(med_docs, storage_context=storage_context_med)
    
        # persist index
        med_index.storage_context.persist(persist_dir="./storage/med")
    
    med_engine = med_index.as_query_engine(similarity_top_k=3)
    print(med_index)
    
    query_engine_tools = [
        QueryEngineTool(
            query_engine=med_engine,
            metadata=ToolMetadata(
                name="med",
                description=(
                    "Provides medical recommendationsi"
                    #"Use a detailed plain text question as input to the tool."
                ),
            ),
        ),
    ]

    llm = OpenAI(model="gpt-3.5-turbo-0613")
    
    agent = ReActAgent.from_tools(
        query_engine_tools,
        llm=llm,
        verbose=True,
        # context=context
    )
    
    #response = agent.chat("what desease ASGHARGHOLI may have?")
    response = agent.chat(prompt)
    #print(str(response))

    return response
