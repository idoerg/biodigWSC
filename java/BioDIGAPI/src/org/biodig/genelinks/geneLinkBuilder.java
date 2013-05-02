package org.biodig.genelinks;

//Class that is used to build a gene object that 
public class geneLinkBuilder {

	public class GeneLinkDataBuilder 
	{


					//Empy variables to be filled later by the user as needed
					String name = "";
					int organismId = 0;
					String uniquename = "";
					
					public GeneLinkDataBuilder setName(String Name) 
					{
						this.name = Name;
						return this;
					}
					
					public GeneLinkDataBuilder setOrganismId(int orgId) 
					{
						this.organismId = orgId;
						return this;
					}
					public GeneLinkDataBuilder setUnqiueName(String UniqueName) 
					{
						this.uniquename = UniqueName;
						return this;
					}

					public geneLinkData build()
					{
						return new geneLinkData(name,organismId,uniquename);
					}
					

	}


}
