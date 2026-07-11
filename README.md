# Awesome Pathology & Spatial-Omics AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of papers on **artificial intelligence for computational pathology, spatial transcriptomics, and single-cell genomics** — with a focus on **predicting gene expression from histology images (H2ST)**, multimodal histo-genomic modeling, foundation models, and biomedical reasoning agents.

![papers](https://img.shields.io/badge/papers-84-blue) ![with%20code](https://img.shields.io/badge/with%20code-52-brightgreen) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md) [![License: CC0](https://img.shields.io/badge/License-CC0-lightgrey.svg)](LICENSE)

Papers span venues including ICML, CVPR, ICLR, NeurIPS, AAAI, Nature / Nature Communications, Science and more (mostly 2025–2026). Each entry links to the paper or its official code. Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Contents

- [🧬 Single-cell & RNA Foundation Models](#single-cell-foundation-models) (9)
- [🔬 Pathology Foundation Models (Knowledge Distillation & Multimodal)](#pathology-foundation-models) (2)
- [🗺️ Spatial-omics Foundation Models](#spatial-foundation-models) (4)
- [🖼️➡️🧬 Histology → Gene Expression Prediction](#histology-to-gene-expression) (19)
- [📈 Spatial Transcriptomics Analysis](#spatial-transcriptomics-analysis) (9)
- [🔎 Single-cell Analysis & Dynamics](#single-cell-analysis) (9)
- [🧫 Computational Pathology (WSI)](#computational-pathology-wsi) (13)
- [🔗 Multimodal Histo-Genomic Fusion & Prognosis](#multimodal-histo-genomics) (4)
- [🤖 LLM Agents & Reasoning](#agents-and-reasoning) (4)
- [💡 Interpretability & Sparse Autoencoders](#interpretability-sae) (4)
- [🧩 Genomic / DNA Language Models](#genomic-language-models) (2)
- [🏁 Benchmarks, Datasets & Toolkits](#benchmarks-datasets-tools) (2)
- [📚 Surveys & Perspectives](#surveys-and-perspectives) (3)

---

<a id="single-cell-foundation-models"></a>

## 🧬 Single-cell & RNA Foundation Models

*Transcriptome-scale pretrained models for single-cell RNA-seq, multi-omics and mRNA sequences.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [Geneformer: Transfer learning enables predictions in network biology](https://www.nature.com/articles/s41586-023-06139-9) | Nature | 2023 | sc RNA-seq, FM | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/epigen/Geneformer) |
| [scGPT: Towards Building a Foundation Model for Single-Cell Multi-omics Using Generative AI](https://github.com/bowang-lab/scgpt) | Nature Methods | 2024 | sc RNA-seq, FM | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/bowang-lab/scgpt) |
| [scMulan: A Multitask Generative Pre-trained Language Model for Single-Cell Analysis](https://github.com/SuperBianC/scMulan) | RECOMB | 2024 | sc RNA-seq, FM | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/SuperBianC/scMulan) |
| [Cell2Sentence: Single-cell Analysis With LLMs](https://github.com/vandijklab/cell2sentence) | bioRxiv | 2025 | sc RNA-seq, FM | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/vandijklab/cell2sentence) |
| [AIDO.Cell: Scaling Dense Representations for Single Cell with Transcriptome-Scale Context](https://www.biorxiv.org/content/10.1101/2024.11.28.625303v1.full.pdf) | NeurIPS | 2024 | Whole Transcriptome, FM, sc RNA-seq | [[paper]](https://www.biorxiv.org/content/10.1101/2024.11.28.625303v1.full.pdf) |
| [CELLama: Foundation Model for Single Cell and Spatial Transcriptomics by Cell Embedding Leveraging Language Model Abilities](https://github.com/portrai-io/CELLama) | Advanced Science | 2025 | sc RNA-seq, FM, spatial transcriptomics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/portrai-io/CELLama) |
| [UCE: Universal cell embedding provides a foundation model for cell biology](https://www.nature.com/articles/s41586-026-10689-z) | Nature | 2026 | sc RNA-seq, FM | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/snap-stanford/UCE) |
| [TranscriptFormer: A generative cell atlas across 1.5 billion years of evolution](https://github.com/czi-ai/transcriptformer) | Science | 2026 | sc RNA-seq, FM | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/czi-ai/transcriptformer) |
| [Orthrus: toward evolutionary and functional RNA foundation models](https://github.com/bowang-lab/Orthrus) | Nature Methods | 2026 | RNA, FM, Mamba | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/bowang-lab/Orthrus) |

[⬆ back to top](#contents)

<a id="pathology-foundation-models"></a>

## 🔬 Pathology Foundation Models (Knowledge Distillation & Multimodal)

*Slide-level pathology FMs built via knowledge distillation from expert vision models (GPFM) and via multimodal knowledge injection from gene expression + pathology reports (mSTAR).*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [GPFM: A generalizable pathology foundation model using a unified knowledge distillation pretraining framework](https://www.nature.com/articles/s41551-025-01488-4) | Nature BME | 2025 |  | [[paper]](https://www.nature.com/articles/s41551-025-01488-4) |
| [mSTAR: A multimodal knowledge-enhanced whole-slide pathology foundation model](https://www.nature.com/articles/s41467-025-66220-x) | Nature Communications | 2025 | WSI | [[paper]](https://www.nature.com/articles/s41467-025-66220-x) |

[⬆ back to top](#contents)

<a id="spatial-foundation-models"></a>

## 🗺️ Spatial-omics Foundation Models

*Foundation models built natively for spatial transcriptomics / proteomics.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [SToFM: a Multi-scale Foundation Model for Spatial Transcriptomics](https://github.com/PharMolix/SToFM) | ICML | 2025 | spatial transcriptomics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/PharMolix/SToFM) |
| [HEIST: A Graph Foundation Model for Spatial Transcriptomics and Proteomics Data](https://github.com/Graph-and-Geometric-Learning/HEIST) | ICLR | 2026 | spatial transcriptomics, Proteomics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/Graph-and-Geometric-Learning/HEIST) |
| [SEAL: Towards Spatial Transcriptomics-driven Pathology Foundation Models](https://github.com/mahmoodlab/SEAL/) | arxiv | 2026 | spatial transcriptomics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/mahmoodlab/SEAL/) |
| [SPATIA: Multimodal Generation and Prediction of Spatial Cell Phenotypes](https://zitniklab.hms.harvard.edu/SPATIA/) | ICML | 2026 | spatial transcriptomics | [[paper]](https://zitniklab.hms.harvard.edu/SPATIA/) |

[⬆ back to top](#contents)

<a id="histology-to-gene-expression"></a>

## 🖼️➡️🧬 Histology → Gene Expression Prediction

*Predicting spatial / bulk gene expression directly from H&E whole-slide images (a.k.a. H2ST).*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [GeneRAG: A Retrieval-Augmented Framework for Spatially Resolved Gene Expression Prediction](https://github.com/HyeongSubKim/GeneRAG) | MICCAI | 2026 | spatial transcriptomics, H2ST, RAG, zero-shot | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/HyeongSubKim/GeneRAG) |
| [STAMP: Fusing Pixels and Genes: Spatially-Aware Learning in Computational Pathology](https://github.com/Hanminghao/STAMP) | ICLR | 2026 | spatial transcriptomics, dataset | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/Hanminghao/STAMP) |
| [Prior knowledge Injection into Deep Learning Models Predicting Gene Expression from Whole Slide Images](https://arxiv.org/pdf/2501.14056) | arxiv | 2025 | spatial transcriptomics, H2ST, Knowledge Injection | [[paper]](https://arxiv.org/pdf/2501.14056) |
| [GenAR: Next-Scale Autoregressive Generation for Spatial Gene Expression Prediction](https://github.com/oyjr/genar) | arxiv | 2025 | spatial transcriptomics, H2ST | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/oyjr/genar) |
| [FLAG: Foundation model representation with Latent diffusion Alignment via Graph for spatial gene expression prediction](https://icml.cc/virtual/2026/poster/60603) | ICML | 2026 | spatial transcriptomics, H2ST | [[paper]](https://icml.cc/virtual/2026/poster/60603) |
| [MoLF: Mixture-of-Latent-Flow for Pan-Cancer Spatial Gene Expression Prediction from Histology](https://susuhu.github.io/MoLF/) | ICML | 2026 | spatial transcriptomics, H2ST, Pan-Cancer | [[paper]](https://susuhu.github.io/MoLF/) |
| [HistoPrism: Unlocking Functional Pathway Analysis from Pan-Cancer Histology via Gene Expression Prediction](https://github.com/susuhu/HistoPrism) | ICLR | 2026 | spatial transcriptomics, H2ST, Pan-Cancer | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/susuhu/HistoPrism) |
| [HINGE: Adapting a Pre-trained Single-Cell Foundation Model to Spatial Gene Expression Generation from Histology Images](https://github.com/donghaifang/HINGE) | CVPR | 2026 | spatial transcriptomics, H2ST, Knowledge Injection | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/donghaifang/HINGE) |
| [HEXST: Hexagonal Shifted-Window Transformer for Spatial Transcriptomics Gene Expression Prediction](https://github.com/QuIIL/HEXST) | ICML | 2026 | spatial transcriptomics, H2ST, Knowledge Injection | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/QuIIL/HEXST) |
| [HiFusion: Hierarchical Intra-Spot Alignment and Regional Context Fusion for Spatial Gene Expression Prediction from Histopathology](https://github.com/Advanced-AI-in-Medicine-and-Physics-Lab/HiFusion) | AAAI | 2026 | spatial transcriptomics, H2ST | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/Advanced-AI-in-Medicine-and-Physics-Lab/HiFusion) |
| [PixNet: From Spots to Pixels: Dense Spatial Gene Expression Prediction from Histology Images](https://github.com/wangzrk/From-Spots-to-Pixels) | CVPR | 2026 | spatial transcriptomics, H2ST | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/wangzrk/From-Spots-to-Pixels) |
| [HyperST: Hierarchical Hyperbolic Learning for Spatial Transcriptomics Prediction](https://github.com/liesgame/HyperST) | CVPR | 2026 | spatial transcriptomics, H2ST | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/liesgame/HyperST) |
| [MCToGene: Predicting Spatial Transcriptomics from Histology Images via High-Order Multi-Cell Interaction Modeling](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Predicting_Spatial_Transcriptomics_from_Histology_Images_via_High-Order_Multi-Cell_Interaction_CVPR_2026_paper.pdf) | CVPR | 2026 | spatial transcriptomics, H2ST | [[paper]](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Predicting_Spatial_Transcriptomics_from_Histology_Images_via_High-Order_Multi-Cell_Interaction_CVPR_2026_paper.pdf) |
| [Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images](https://github.com/naivete5656/CPNN) | CVPR | 2026 | H2ST, sc RNA-seq, spatial transcriptomics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/naivete5656/CPNN) |
| [SpaHGC:Cross-Slice Knowledge Transfer via Masked Multi-Modal Heterogeneous Graph Contrastive Learning for Spatial Gene Expression Inference](https://github.com/wenwenmin/SpaHGC) | CVPR | 2026 | spatial transcriptomics, H2ST | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/wenwenmin/SpaHGC) |
| [FEAST: Fully Connected Expressive Attention for Spatial Transcriptomics](https://github.com/starforTJ/FEAST) | CVPR | 2026 | spatial transcriptomics, H2ST | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/starforTJ/FEAST) |
| [Dual-Path Knowledge-Augmented Contrastive Alignment Network for Spatially Resolved Transcriptomics](https://github.com/coffeeNtv/DKAN) | AAAI | 2026 | Oral, spatial transcriptomics, H2ST, Knowledge Injection | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/coffeeNtv/DKAN) |
| [Multi-View Hierarchical Alignment Learning for Spatial Transcriptomics](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_Multi-View_Hierarchical_Alignment_Learning_for_Spatial_Transcriptomics_CVPR_2026_paper.pdf) | CVPR | 2026 | spatial transcriptomics | [[paper]](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_Multi-View_Hierarchical_Alignment_Learning_for_Spatial_Transcriptomics_CVPR_2026_paper.pdf) |
| [GSAT-RAG: Open-Set Spatial Gene Expression Prediction from Histological Images via Retrieval-Augmented Generation](https://openaccess.thecvf.com/content/CVPR2026F/papers/Wu_Open-Set_Spatial_Gene_Expression_Prediction_from_Histological_Images_via_Retrieval-Augmented_CVPRF_2026_paper.pdf) | CVPR | 2026 | spatial transcriptomics, H2ST, sc RNA-seq | [[paper]](https://openaccess.thecvf.com/content/CVPR2026F/papers/Wu_Open-Set_Spatial_Gene_Expression_Prediction_from_Histological_Images_via_Retrieval-Augmented_CVPRF_2026_paper.pdf) |

[⬆ back to top](#contents)

<a id="spatial-transcriptomics-analysis"></a>

## 📈 Spatial Transcriptomics Analysis

*Denoising, imputation, representation learning, niche & region modeling on ST data.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [Global Context-aware Representation Learning for Spatially Resolved Transcriptomics](https://github.com/yunhak0/Spotscape) | ICML | 2025 | spatial transcriptomics, Imputation | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/yunhak0/Spotscape) |
| [SUICA: Learning Super-high Dimensional Sparse Implicit Neural Representations for Spatial Transcriptomics](https://github.com/Szym29/SUICA) | ICML | 2025 | spatial transcriptomics, Imputation | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/Szym29/SUICA) |
| [SpaEF: Spatially Resolved Transcriptomics Data Element-Wise Denoising Framework Powered by Large Models](https://github.com/Zekuan-Shang/SpaEF) | ICML | 2026 | spatial transcriptomics, Denoising | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/Zekuan-Shang/SpaEF) |
| [InfoGlobe: Local-and-Global Information-Preserving Statistical Manifold Learning for Single-Cell Transcriptomics](https://openreview.net/forum?id=LMrsqvShfy) | ICML | 2026 | spatial transcriptomics, sc RNA-seq, Compression | [[paper]](https://openreview.net/forum?id=LMrsqvShfy) |
| [STRank: Learning to Relative Expression under Batch Effects and Stochastic Noise in Spatial Transcriptomics](https://github.com/naivete5656/STRank) | NeurIPS | 2025 | spatial transcriptomics, H2ST | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/naivete5656/STRank) |
| [Modeling Microenvironment Trajectories on Spatial Transcriptomics with NicheFlow](https://arxiv.org/pdf/2511.00977) | NeurIPS | 2025 | spatial transcriptomics, Temporal Dynamics | [[paper]](https://arxiv.org/pdf/2511.00977) |
| [SpaCRD: Multimodal Deep Fusion of Histology and Spatial Transcriptomics for Cancer Region Detection](https://github.com/wenwenmin/SpaCRD) | AAAI | 2026 | Oral, spatial transcriptomics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/wenwenmin/SpaCRD) |
| [BRGMAR: Bulk RNA-seq Guided Multi-modal Detection of Anomalous Regions in Human Cancer via Spatial Transcriptomics](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Bulk_RNA-seq_Guided_Multi-modal_Detection_of_Anomalous_Regions_in_Human_CVPR_2026_paper.pdf) | CVPR | 2026 | Bulk RNA-seq, Biology, spatial transcriptomics, WSI | [[paper]](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Bulk_RNA-seq_Guided_Multi-modal_Detection_of_Anomalous_Regions_in_Human_CVPR_2026_paper.pdf) |
| [scMRDR: A Scalable and Flexible Framework for Unpaired Single-Cell Multi-Omics Data Integration](https://github.com/sjl-sjtu/scMRDR) | NeurIPS | 2025 | sc RNA-seq, spatial transcriptomics, Proteomics, scATAC-seq | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/sjl-sjtu/scMRDR) |

[⬆ back to top](#contents)

<a id="single-cell-analysis"></a>

## 🔎 Single-cell Analysis & Dynamics

*Trajectories, gene regulatory networks, generation, perturbation and continual learning.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [Learning Explicit Single-cell Dynamics Using ODE Representations](https://github.com/czi-ai/cell-mnn) | ICLR | 2026 | sc RNA-seq, Temporal Dynamics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/czi-ai/cell-mnn) |
| [LGP-OT: Modeling Temporal scRNA-seq Data with Latent Gaussian Process and Optimal Transport](https://github.com/YigitBalik/LGP-OT) | ICML | 2026 | sc RNA-seq, Temporal Dynamics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/YigitBalik/LGP-OT) |
| [CellBRIDGE: Learning Cellular Trajectories via Interaction-Aware Alignment](https://github.com/nicolashuynh/cellbridge) | ICML | 2026 | sc RNA-seq, Temporal Dynamics | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/nicolashuynh/cellbridge) |
| [UGRN: Towards Universal Gene Regulatory Network Inference](https://github.com/simpleshinobu/UGRN) | ICML | 2026 | sc RNA-seq | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/simpleshinobu/UGRN) |
| [scChord: A Probabilistic Manifold Rectification Framework for RNA-to-Protein Translation](https://github.com/Jave-Zhang/scChord) | ICML | 2026 |  | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/Jave-Zhang/scChord) |
| [SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention](https://github.com/fdu-wangfeilab/sc-save) | ICLR | 2026 | sc RNA-seq | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/fdu-wangfeilab/sc-save) |
| [PRESCRIBE: Predicting Single-Cell Responses with Bayesian Estimation](https://github.com/Bunnybeibei/PRESCRIBE) | NeurIPS | 2025 | sc RNA-seq | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/Bunnybeibei/PRESCRIBE) |
| [Gene Incremental Learning for Single-Cell Transcriptomics](https://github.com/simpleshinobu/scbenchmark) | AAAI | 2026 | sc RNA-seq | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/simpleshinobu/scbenchmark) |
| [scPilot: Large Language Model Reasoning for Automated Single-Cell Analysis](https://github.com/maitrix-org/scPilot) | NeurIPS | 2025 | Reasoning, sc RNA-seq | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/maitrix-org/scPilot) |

[⬆ back to top](#contents)

<a id="computational-pathology-wsi"></a>

## 🧫 Computational Pathology (WSI)

*Multiple-instance learning, survival, retrieval, segmentation and image generation on slides.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [Exploiting Low-Dimensional Manifold of Features for Few-Shot Whole Slide Image Classification](https://github.com/BearCleverProud/MR-Block) | ICLR | 2026 | WSI | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/BearCleverProud/MR-Block) |
| [ABMILX: Revisiting End-to-End Learning with Slide-level Supervision in Computational Pathology](https://github.com/DearCaat/E2E-WSI-ABMILX) | NeurIPS | 2025 | WSI | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/DearCaat/E2E-WSI-ABMILX) |
| [FOCUS: Knowledge-enhanced Adaptive Visual Compression for Few-shot Whole Slide Image Classification](https://github.com/dddavid4real/focus) | CVPR | 2025 | WSI | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/dddavid4real/focus) |
| [PMIL: Shapley Values-enabled Progressive Pseudo Bag Augmentation for Whole-Slide Image Classification](https://github.com/RenaoYan/PMIL) | IEEE TMI | 2024 | WSI | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/RenaoYan/PMIL) |
| [MAMMOTH: Mixture of Mini Experts: Overcoming the Linear Layer Bottleneck in Multiple Instance Learning](https://github.com/mahmoodlab/MAMMOTH) | ICLR | 2026 | WSI | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/mahmoodlab/MAMMOTH) |
| [Dual-Prototype Evidential Fusion for Uncertainty-Aware and Interpretable Whole Slide Image Survival Prediction](https://github.com/YuchengXing99/DPsurv) | ICML | 2026 | WSI | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/YuchengXing99/DPsurv) |
| [PathCTM: Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning](https://github.com/JSGe-AI/PathCTM) | ICML | 2026 |  | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/JSGe-AI/PathCTM) |
| [Accurate and Scalable Multimodal Pathology Retrieval via Attentive Vision-Language Alignment](https://arxiv.org/abs/2510.23224) | arxiv | 2025 |  | [[paper]](https://arxiv.org/abs/2510.23224) |
| [Segment Anything in Pathology Images with Natural Language](https://arxiv.org/pdf/2506.20988) | arxiv | 2025 |  | [[paper]](https://arxiv.org/pdf/2506.20988) |
| [Generative AI for misalignment-resistant virtual staining to accelerate histopathology workflows](https://www.nature.com/articles/s41467-026-71038-2) | Nature Communications | 2026 |  | [[paper]](https://www.nature.com/articles/s41467-026-71038-2) |
| [Conditional Visual Autoregressive Modeling for Pathological Image Restoration](https://arxiv.org/pdf/2507.17388v1) | ICCV | 2025 |  | [[paper]](https://arxiv.org/pdf/2507.17388v1) |
| [TRIDENT: A Trimodal Cascade Generative Framework for Drug and RNA-Conditioned Cellular Morphology Synthesis](https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_TRIDENT_A_Trimodal_Cascade_Generative_Framework_for_Drug_and_RNA-Conditioned_CVPR_2026_paper.pdf) | CVPR | 2026 |  | [[paper]](https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_TRIDENT_A_Trimodal_Cascade_Generative_Framework_for_Drug_and_RNA-Conditioned_CVPR_2026_paper.pdf) |
| [Automated Detection of BK Virus in H&E Whole-Slide Images Using Weakly-Supervised Deep Learning and Interpretable Morphological Biomarkers](https://papers.miccai.org/miccai-2025/paper/5442_paper.pdf) | MICCAI | 2025 | WSI | [[paper]](https://papers.miccai.org/miccai-2025/paper/5442_paper.pdf) |

[⬆ back to top](#contents)

<a id="multimodal-histo-genomics"></a>

## 🔗 Multimodal Histo-Genomic Fusion & Prognosis

*Fusing pathology images with genomics / proteomics for molecular prediction and prognosis.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [Genome-Anchored Foundation Model Embeddings Improve Molecular Prediction from Histology Images](https://arxiv.org/abs/2506.19681) | arxiv | 2025 | Bulk RNA-seq, WSI | [[paper]](https://arxiv.org/abs/2506.19681) |
| [G-HANet: Histo-Genomic Knowledge Distillation For Cancer Prognosis From Histopathology Whole Slide Images](https://ieeexplore.ieee.org/abstract/document/10830530) | IEEE TMI | — | WSI, Bulk RNA-seq, CNV, Gene mutation status | [[paper]](https://ieeexplore.ieee.org/abstract/document/10830530) |
| [HFGPI: Advancing Cancer Prognosis with Hierarchical Fusion of Genomic, Proteomic and Pathology Imaging Data from a Systems Biology Perspective](https://arxiv.org/abs/2603.13787) | CVPR | 2026 | Bulk RNA-seq, Proteomics, WSI | [[paper]](https://arxiv.org/abs/2603.13787) |
| [CARE: A Molecular-Guided Foundation Model with Adaptive Region Modeling for Whole Slide Image Analysis](https://github.com/zdipath/CARE) | CVPR | 2026 | Bulk RNA-seq, Proteomics, WSI | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/zdipath/CARE) |

[⬆ back to top](#contents)

<a id="agents-and-reasoning"></a>

## 🤖 LLM Agents & Reasoning

*Agentic and reasoning systems for pathology, spatial omics and single-cell analysis.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [NOVA: An Agentic Framework for Automated Histopathology Analysis and Discovery](https://github.com/microsoft/nova-agent) | arxiv | 2025 | Reasoning, WSI | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/microsoft/nova-agent) |
| [SP-Mind: An Autonomous Reasoning Agent for Spatial Proteomics](https://github.com/tomtommyyuan/spmind) | ICML | 2026 | Reasoning, Proteomics, dataset | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/tomtommyyuan/spmind) |
| [From Conflict to Consensus: Boosting Medical Reasoning via Multi-Round Agentic RAG](https://github.com/NJU-RL/MA-RAG) | ICML | 2026 | Reasoning | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/NJU-RL/MA-RAG) |
| [Artificial intelligence agents in cancer research and oncology](https://www.nature.com/articles/s41568-025-00900-0) | Nature Review Cancer | 2026 |  | [[paper]](https://www.nature.com/articles/s41568-025-00900-0) |

[⬆ back to top](#contents)

<a id="interpretability-sae"></a>

## 💡 Interpretability & Sparse Autoencoders

*Concept discovery and mechanistic interpretability of pathology / bio foundation models.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [Explain Any Pathological Concept: Discovering Hierarchical Explanations for Pathology Foundation Models](https://papers.miccai.org/miccai-2025/paper/1641_paper.pdf) | MICCAI | 2025 |  | [[paper]](https://papers.miccai.org/miccai-2025/paper/1641_paper.pdf) |
| [Interpreting Genomic Language Models using Sparse Autoencoders](https://github.com/akira-nair/glm-sae-interpretability) | ICML | 2026 | Sparse Autoencoder | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/akira-nair/glm-sae-interpretability) |
| [ProtSAE: Disentangling and Interpreting Protein Language Models via Semantically-Guided Sparse Autoencoders](https://github.com/nju-websoft/ProtSAE) | AAAI | 2026 | Proteomics, Sparse Autoencoder | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/nju-websoft/ProtSAE) |
| [Dissecting and directing pathology foundation models](https://www.biorxiv.org/content/10.64898/2026.06.12.731496v1.full.pdf) | arxiv | 2026 | Sparse Autoencoder | [[paper]](https://www.biorxiv.org/content/10.64898/2026.06.12.731496v1.full.pdf) |

[⬆ back to top](#contents)

<a id="genomic-language-models"></a>

## 🧩 Genomic / DNA Language Models

*Tokenization, representation and evaluation of DNA / genomic foundation models.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [PatchDNA: A Flexible and Biologically-Informed Alternative to Tokenization for DNA](https://openreview.net/forum?id=AFZeojzjoG) | ICLR | 2026 |  | [[paper]](https://openreview.net/forum?id=AFZeojzjoG) |
| [TOKENIZATION TO TRANSFER: DO GENOMIC FOUNDATION MODELS LEARN GOOD REPRESENTATIONS?](https://github.com/m42-health/gfm-random-eval) | ICLR | 2026 |  | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/m42-health/gfm-random-eval) |

[⬆ back to top](#contents)

<a id="benchmarks-datasets-tools"></a>

## 🏁 Benchmarks, Datasets & Toolkits

*Open benchmarks, multicentric datasets and data-processing toolkits.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [DALPHIN: Benchmarking Digital Pathology AI Copilots Against Pathologists on an Open Multicentric Dataset](https://dalphin.grand-challenge.org/) | — | — | dataset, Reasoning | [[paper]](https://dalphin.grand-challenge.org/) |
| [Accelerating Data Processing and Benchmarking of AI Models for Pathology](https://github.com/mahmoodlab/trident/) | — | — | Toolkit | [![code](https://img.shields.io/badge/code-black?logo=github)](https://github.com/mahmoodlab/trident/) |

[⬆ back to top](#contents)

<a id="surveys-and-perspectives"></a>

## 📚 Surveys & Perspectives

*Review articles and perspectives on the field.*

| Title | Venue | Year | Topics | Links |
|---|:--:|:--:|---|:--:|
| [A Survey of Pathology Foundation Model: Progress and Future Directions](https://arxiv.org/abs/2504.04045) | arxiv | 2025 |  | [[paper]](https://arxiv.org/abs/2504.04045) |
| [A Survey on Foundation Language Models for Single-cell Biology](https://aclanthology.org/2025.acl-long.26.pdf) | ACL | 2025 | sc RNA-seq | [[paper]](https://aclanthology.org/2025.acl-long.26.pdf) |
| [Large Language Models for Transforming Healthcare: A Perspective on DeepSeek-R1](https://onlinelibrary.wiley.com/doi/full/10.1002/mef2.70021) | — | 2025 |  | [[paper]](https://onlinelibrary.wiley.com/doi/full/10.1002/mef2.70021) |

[⬆ back to top](#contents)

---

## Legend

- **H2ST** — *Histology-to-Spatial-Transcriptomics*: predicting spatial gene expression from H&E images.
- **WSI** — Whole-Slide Image. **FM** — Foundation Model. **SAE** — Sparse Autoencoder.
- ![code](https://img.shields.io/badge/code-black?logo=github) marks entries with an official code release.

## Contributing

Found a missing paper or a broken link? Please open a pull request or issue. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the maintainers have waived all copyright and related or neighboring rights to this work.
