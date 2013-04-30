package images;

import java.util.List;

public class imageDataBuilder {


				//Empy variables to be filled later by the user as needed
				String alternateText = "";
				String imgDescription = "";
				List<Organism> imgOrganisms = null;
				
				
				public imageDataBuilder setAlternateText(String alternateText) 
				{
					this.alternateText = alternateText;
					return this;
				}
				public imageDataBuilder setImgDescription(String imgDescription) 
				{
					this.imgDescription = imgDescription;
					return this;
				}
				public imageDataBuilder setImgOrganisms(List<Organism> imgOrganisms) 
				{
					this.imgOrganisms = imgOrganisms;
					return this;
				}

				public imageData build()
				{
					return new imageData(alternateText,imgDescription,imgOrganisms);
				}
				

}
