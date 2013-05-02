package org.biodig.images;

import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.UriBuilder;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.UniformInterfaceException;
import com.sun.jersey.api.client.WebResource;
import com.sun.jersey.api.client.config.ClientConfig;
import com.sun.jersey.api.client.config.DefaultClientConfig;
import com.sun.jersey.client.apache.ApacheHttpClient;
import com.sun.jersey.multipart.FormDataMultiPart;
import com.sun.jersey.multipart.file.FileDataBodyPart;

import com.google.gson.Gson;
import java.awt.BorderLayout;
import java.awt.Image;
import java.io.File;
import java.net.URL;
import java.util.List;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.xml.ws.http.HTTPException;

import org.biodig.*;

public class JerseyGetImageData 
{
	// Location of the server the API draws from
	static String imageBioDIG_URL = "http://wan1.mbi.muohio.edu/dome/";


	public static void main(String[] args) 
	{
		getImageInfo("12");
	}
	
	// GET METHOD
	public static void getImageInfo(String imgId) {
		try
		{
		ClientConfig config = new DefaultClientConfig();
		Client client = Client.create(config);
		WebResource service = client.resource(UriBuilder.fromUri("http://192.168.142.128/api/images?id="+imgId).build());
		ClientResponse response = service.accept(MediaType.TEXT_HTML).get(ClientResponse.class);
	//---Used for debugging purposes to check the status of the Get call----
		//System.out.println(response.toString());

		String imageMetaData = service.accept(MediaType.APPLICATION_JSON).get(String.class);
		//System.out.println(imageMetaData);
		
		//Creation of objects to parse the raw JSON data
		imageData img = new Gson().fromJson(imageMetaData, imageData.class);

		System.out.println(img.toString());
		}
		catch(UniformInterfaceException e)
		{
			System.out.println("The image id you have provided does not exist. Please enter a valid image Id.");
			e.printStackTrace();
		}
	}
	
	public static void getImage(String imageURL)
	{
		try 
		{
		 //Flushes the image and grabs a link 
		  Image image = null; 
		  URL url = new URL("http://192.168.142.128/media/pictures/1366322421.631cfcbd94d4f27a1f6c8719e611eb46dd.png"); image = ImageIO.read(url); // Use a label to display the image
		  JFrame frame = new JFrame();
		  
		  JLabel lblimage = new JLabel(new ImageIcon(image));
		  frame.getContentPane().add(lblimage, BorderLayout.CENTER);
		  frame.setSize(300, 400); frame.setVisible(true); 
		  JPanel mainPanel = new JPanel(new BorderLayout()); mainPanel.add(lblimage);
		  //Displays the image. frame.add(mainPanel);
		  frame.setVisible(true);
		  
		 } 
	catch (Exception e) 
	{
		  System.out.println("The image id you have provided does not exist. Please enter a valid image Id."); 
	}

	}
	
	static public void editImageInfo(String oldImgId, imageData img)
	{
		try
		{
			//opens connection with client
			ClientConfig cc = new DefaultClientConfig();
	        Client client = Client.create(cc);
	        WebResource resource = client.resource("http://192.168.142.128/api/images");
			//Put
			
	        //Adds parameters to be posted
		        FormDataMultiPart form = new FormDataMultiPart();
		        //Logic check to determine what is posted to the image
		        if(img.getAltText()!="" && img.getAltText()!=null)
		        form.field("altText",img.getAltText());
		        if(img.getDescription()!="" && img.getDescription()!=null)
		        form.field("description",img.getDescription());
		        if(img.getOrganisms()!=null)
		        form.field("organisms",img.getOrganisms().toString());
		        ClientResponse response = resource.type(MediaType.MULTIPART_FORM_DATA).put(ClientResponse.class, form);
		        System.out.println(response.toString());
			
				System.out.println("The image id you have provided does not exist. Please enter a valid image Id.");
			}
		
		catch(Exception e)
		{
			e.printStackTrace();
		}
		
         
	}

	//Adds an image, file path is required.
	static public void addImage(String filepath, imageData img)
	{
		try
		{
			//opens connection with client
			ClientConfig cc = new DefaultClientConfig();
	        Client client = Client.create(cc);
	        WebResource resource = client.resource("http://192.168.142.128/api/images");
			//Put
			
	        
	        
	        //Adds parameters to be posted
	        FormDataMultiPart form = new FormDataMultiPart();
	        File file = new File(filepath);
	        //Logic check to determine what is posted to the image
	        if(img.getAltText()!="" && img.getAltText()!=null)
	        form.field("altText",img.getAltText());
	        if(img.getDescription()!="" && img.getDescription()!=null)
	        form.field("description",img.getDescription());
	        if(img.getOrganisms()!=null)
	        form.field("organisms",img.getOrganisms().toString());
	        form.bodyPart(new FileDataBodyPart("image", file, MediaType.MULTIPART_FORM_DATA_TYPE));
	        ClientResponse response = resource.type(MediaType.MULTIPART_FORM_DATA).post(ClientResponse.class, form);
	        System.out.println(response.toString());
		}
		catch(HTTPException e)
		{
			System.out.println("The image id you have provided does not exist. Please enter a valid image Id.");
		}
	}
	
	//Deletes the image, with the metadata using Apache HTTP Client
	static public void deleteImage(String imgId)
	{
		try
		{
			//opens connection with client
			ClientConfig cc = new DefaultClientConfig();
	        Client client = new ApacheHttpClient();
	        WebResource resource = client.resource("http://192.168.142.128/api/images");
	        FormDataMultiPart form = new FormDataMultiPart();

	        form.field("id",imgId);


	       resource.type(MediaType.MULTIPART_FORM_DATA).delete(form);

	       System.out.println("Image "+imgId+" has been deleted successfully!");
		}
		catch(HTTPException e)
		{
			System.out.println("The image id you have provided does not exist. Please enter a valid image Id.");
		}
	}
}