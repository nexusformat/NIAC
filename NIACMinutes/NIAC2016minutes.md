# NIAC 2016 Minutes

October, 13-14, 2016 in Copenhagen, COBIS Building, M10

## Thursday, October, 13

Welcome from Tobias, organizational tidbits

Introduction round

### Topics

- **NXtransformations, NXmx,**, done
- **NXreflections, NXprocess**, done
- WWW-site update, done
- **Streaming NeXus**, done
- NXdirecttof
- Variable length strings, done
- NXcontainer
- Problems with storing scan information
- Versioning, done 
- How to increase adoption, done
- 2014 Attributes, done
- **NXcansas**, done
- NXdata, required?, plottable?
- **NXsample**, done 
- „NXshape“, CSG in NeXus
- Weight
- Update on NexPy
- cnxvalidate presentation, done
- HDF5 discussion, done
- How to increase NeXus adoption?, done


### Membership Renewals

Ray Osborn unanimously confirmed as representative of ANL in NIAC

Stephen Cottrell unanimously confirmed as representative of the musr community in NIAC

Armando Sole unanimously accepted as ESRF representative in NIAC

Joachim Wuttke has expired as NIAC member and does not wish to maintain his membership. There will be no new representative for FRM-2. 

 
### cnxvalidate

Presentation by Mark Koennecke

Discussion on validating units and units itself. 

Action Items:

- Issue on cnxvalidate: research better validation of units, may be with UDunits, or else.
- Revisit units in the technical committee: interested parties: Eugen, Herbert, Aaron, Ricardo, aim for a representative of Mantid 

### canSAS

Pete Jemian presented the canSAS application definition. There is a mapping  from canSAS to NeXus. 

There was some discussion on this. The result was that the definition will be revised to only represent the processed data (I(Q)) use case. To be revisited once this is done. May be tomorrow. 

### WWW-Site

Ray presented his suggestion for a revised NeXus WWW-site. The main point is to make it look more modern. Also it is to be generated with sphinx which makes it easier to restyle it using sphinx styles. 

Still needs some work, revisit at NeXus Telco. Then make it mobile friendly. If we can do this easily with Sphinx. 

 
## Thursday afternoon

### NXmx, NXtransformations

Herbert is presenting proposed changes for NXmx-1.5. 

NXmx is adding a NXdetector_group for documenting detectors better to humans. They have funny detectors with segments which move diagonally with regards to the detector center. 

Added an optional third detector dimension. This is a data organizational dimension. 

There is some discussion about understanding this. 

Changes in NXbeam for polychromatic beams in the application definition. As optional, added in order to be able to validate this. 

Flux may need two values, NXbeam defines flux is flux per unit area. The additional flux is a rate: photons/second. To be called total_flux.

Adding incident_beam_size which is a 2 value array of FWHM (when gaussian) or a diameter (if it is a top hat) or 2 sizes for a rectangular beam. 

Changes to NXmx **accepted by consensus** after a little discussion with no objection. 

 
Herberts presents changes to NXtransformations. 

Axis rotation ranges are being added. Crystallographers want that for emotional reasons. The use case is the oscillation method. 

Under discussion this changed to: 

These three proposals to change NXtransformations below where unanimously accepted for by vote:  

- AXIS_end
- AXIS_increment_set. This is the set value for the oscillation range in an oscillation experiment. 
- The actual AXIS value is the start of the oscillation. This needs to be updated in the documentation. 


The **general** axis is highly contentious and not very well understood.  Herbert says that a general axis could also be expressed as a translation. 

The end of this: Aaron and Herbert provide better documentation and examples. We also half agreed to drop the transformation_type attribute for the general axis. This will be  deferred until we understand this better. 
  
### Dinner

Very nice dinner at taarnet.dk in a high security environment with x-ray. 

## Friday

David Mannicke initially missing. 

### Election of Officers

Tobias Richter confirmed as chair with one abstain, 11 yes

Mark Koennecke confirmed as executive secretary with one abstain, yes 11

Eugen Wintersberger confirmed as technical release manager with one abstain, yes 11

Pete Jemian confirmed as documentation and definition release manager, 12 yes


### Streaming NeXus

Mark Koennecke presented the results of the code camp discussion as a proposal. 

We accepted the renaming NXevent_data fields to what Freddie presented and is being used at SNS and ISIS. All yes.

- scaling_factor as attribute to the time fields in NXlog, NXevent_data. If the scaling_factor is there the time units refer to the units after scaling, 12 yes
- NXlog clarification, 12 yes 
- cue_time_zero, cue_index as optional fields added to NXlog and NXevent_data, they always index into the main time/data arrays.  12 yes
- The structure with replacing fields with NXlog or NXevent_data is accepted, 12 yes

No majority for summarizing the streamed data in NXdata. 
 

Action Item: Mark Basham to report on VDS performance in june. Based on that report we decide if NeXus does need an own segmentation scheme. 


### NXreflections

Presentation by Aaron Brewster. The use case is to store intermediate results 
 
Discussing NXreflections in more detail:

- H,K,L change to NX_number for incommensurate structures
- Discussion on flags, change to bitfield, no enum for efficiency 
- Expand the description of partiality
- Need to keep mm and pixel positions because of parallax
- Write out predicted and observed
- Drop the mm in names, rather use units
- bounding_box as array, document the usage
- Spell out background
- Drop the val on the intensities, keep the _var version
- overlaps is a list of overlapped reflections. This is a ragged array. As the code is not in place we defer it for now. 
- Add polar_angle and azimuthal_angle

Accepted as a base class with 12 yes, with the changes listed above. We trust Aaron to apply the changes. 



### NXsample

Tobias Richter presents suggested changes to NXsample.

- Happy with unit cell a, b, c and angles
- Happy with additional sample types: buffers etc
- Division into  NXsample_component base classes, one per component

Accepted with 12 yes

Some details deferred.

### NXcansas again

Pete Jemian presenting the canSAS application definition revised from feedback of yesterday. 

There was some doubt about this is what the canSAS group wants. 

We accept NXcansas with NXinstrument made optional, 8 yes, 4 abstain 

### Variable length strings

Short discussion on fixed versus variable length strings. 

We accept both variable and fixed length strings, readers have to support both, 11 yes, 1 no

### Versioning

Short discussion on the versioning proposal as presented by Mark Koennecke from the result of the code camp.

Herbert made the comment to improve the workflow in this way:

- You make the change to NXDL and change the version in the NXDL file
- You build a manual and commit it into the repository
- Then you tag the git repository

The proposal was accepted on probation with 12 yes. To be revisited at the next NIAC in order to check if it works.

### Adoption of NeXus

- Convincing scientists
- Pete: use it and make this public
- Herbert: NeXus is required for performance, performance problems, 
- Eugen: users do not want it because analysis tools do not support it, the chicken-egg problem
- Sociological problems: to slow, social problems with NIAC
- From WWW-site point to tools which can plot NeXus, downloadable applications, 
- NexPy and DAWN as general plotting tools
- Pipelines from raw data to processed data
- We spend a good deal of time on raw data formats. This is used for archiving at facilities, not for data exchange.
- Now we are at a place where we understand so much about data that no one else understands us any more.
- Herberts recommends us to listen: where are the needs, Aaron seconds with the question: how we can I help you to solve your scientific problem?
- Ray requests  support for NeXpy 

We ended the discussion on a time limit.  

 
### NXdata

The problem: required group, some cases where no sensible default plot can be provided. 

Change the documentation: make it clear that NXdata should be there but can be omitted if no sensible plot can be provide, 
12 yes. 

### 2014 Attributes

Pete Jemian has a modified version of application definitions with the 2014 attributes applied. This is the signal, axes definitions as group attributes. When changing application definitions consider the code in that branch. 

This is informational.   

## Participants

David Maennicke, ANSTO

Ricardo Ferraz Leal, ORNL

Aaron Brewster, Lawrence Berkely Lab

Ray Osborn, ANL

Ben Watts, SLS, PSI

Jiro Suzuki, KEK

Freddy Akeroyd, ISIS

Eugen Wintersberger, DESY

Alfonso Mukhai, DMSC, (Guest)

Mark Basham, Diamond

Herbert Bernstein, for CIF

Tobias Richter, ESS

Mark Koennecke, SINQ, PSI 

Pete Jemian, APS, part-time attendant by Hangout
