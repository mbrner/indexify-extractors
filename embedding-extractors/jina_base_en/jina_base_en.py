from typing import List
from indexify_extractor_sdk import Content
from indexify_extractor_sdk.base_embedding import (
    BaseEmbeddingExtractor,
    EmbeddingInputParams,
)
from transformers import AutoModel

class JinaEmbeddingsBase(BaseEmbeddingExtractor):
    name = "tensorlake/jina-embeddings-base-en"
    description = "Jina AI Base Embedding Model. HF Link - https://huggingface.co/jinaai/jina-embeddings-v2-base-en"
    python_dependencies = ["torch", "transformers"]
    system_dependencies = []

    def __init__(self):
        super(JinaEmbeddingsBase, self).__init__(max_context_length=512)
        self._model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-en', trust_remote_code=True)

    def extract_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self._model.encode(texts).tolist()


if __name__ == "__main__":
    JinaEmbeddingsBase().run_sample_input()
