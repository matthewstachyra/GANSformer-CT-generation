# GANSformer-CT-generation
Overview
- The goal was to generate fake brain CTs using the new GANSformer architecture.
- GANSformer combines GANS with the Transformer architecture to permit the GAN to attend to and model local object relationships.
- Target metrics were an FID <100 and fooling a well known medical imaging classifer (MONAI).
- First trained on a larger set of lung CTs, then transfered to be fine tuned for a smaller set of brain CTs.
- Brain CTs generated were of high quality. Final FID scores <40 and MONAI classifier had AUC of 0.54 and 0.48/0.52 precision in binary classification task.

Tools, datasets
- GANSformer (2021): https://github.com/dorarad/gansformer 
- MONAI: https://github.com/Project-MONAI
- Lung CTs dataset: COVIDx CT-2 (https://www.kaggle.com/hgunraj/covidxct)
- Brain CTs dataset: Qure.AI CQ500 (http://headctstudy.qure.ai/dataset)

Problem Statement
- Machine learning models augment professional opininon for diagnostics and prognostics. However, they require a large number of images to be trained and often there are not often or not often high quality or not often correct modality images. Device makers and hospitals generally don’t open up their data to the general research community. There are frequently complex privacy laws to navigate, and device makers don’t find it beneficial to share things that might give away their competitive advantage. 

Contributions
- Testing GANsformer with medical images. (To our knowledge, GANsformer hasn’t been applied/tested with medical images, in part due to how new it is. With more work like this, the field learns where GANsformer performs particularly well versus other methods and its use can propagate there.)
- (Successfully) generating plausible CT scans using GAN to expand existing limited datasets. 
- Trying new analysis technique for assessing performance of GAN. (We tried to use an existing medical image classifier to see how will it does at detecting the generated images. As we expected, for the GANsformer, the classifier performed no better than chance.)

Future work
- Adding conditional layers to the model should be explored. As the dataset consists of multiple slices for a given patient, there is a volumetric relationship between the different slices which aren’t captured by the GANSFORMER model. Inspired by the work in Conditional GANs, one can apply an additional layer to the images populated with the image slice number. This would allow the model to learn the difference between a slice toward the top of the head, versus a slice around eye level.  
