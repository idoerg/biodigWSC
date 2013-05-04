package images;

import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.MultivaluedMap;
import javax.ws.rs.core.UriBuilder;
import javax.xml.ws.http.HTTPException;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;
import com.sun.jersey.api.client.config.ClientConfig;
import com.sun.jersey.api.client.config.DefaultClientConfig;
import com.sun.jersey.client.apache.ApacheHttpClient;
import com.sun.jersey.core.util.MultivaluedMapImpl;
import com.sun.jersey.multipart.FormDataMultiPart;
import com.sun.jersey.multipart.file.FileDataBodyPart;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

import java.awt.BorderLayout;
import java.awt.Image;
import java.io.File;
import java.net.URI;
import java.net.URL;
import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class JerseyGetImageData 
{
	//Local Variables used in the methods.
	private JsonParser jsonParser = null;
	private JsonArray MyDIGArray = null;
	private String URL;
	private String mediaType = "MediaType.APPLICATION_JSON";
	private ClientConfig config = null;
	private Client client = null;
	private WebResource service = null;
	private String requestpath;
	
	//Constructor that creates the information needed for API calls.
	public JerseyGetImageData ( String URL ) {
		this.URL = URL;
		this.config = new DefaultClientConfig();
		this.client = Client.create(config);
		this.service = client.resource(getBaseURI());
	}
	
	//Converts a string to a URL compatable with WebResource.
	public URI getBaseURI() 
	{
		return UriBuilder.fromUri(URL).build();
	}
		
	// GET METHOD
	//Uses MultivaluedMap to process the information
	public imageData getImageInfo(int imgId) {
		
			requestpath = "images";
			MultivaluedMap params = new MultivaluedMapImpl();
			params.add("id",Integer.toString(imgId));

			String info = (service.path(requestpath).queryParams(params).accept(mediaType).get(String.class));
			System.out.println(info.toString());

			Gson myGson = new Gson();
			jsonParser = new JsonParser();
			JsonElement tagSelement= jsonParser.parse(info);
			imageData newImageData = myGson.fromJson(tagSelement, imageData.class);
			return newImageData;
		
	}
	
	//Test to retrieve the image and display the image file.
	public static void getImage(String imageURL)
	{
		try 
		{
		 //Flushes the image and grabs a link 
		  Image image = null; 
		  URL url = new URL(imageURL); image = ImageIO.read(url); // Use a label to display the image
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
	//Edits a pre-existing image with new information.
	//Had to use the FormData due to POST being an arseface(Was not working with MultivaluedMap)
	public void editImageInfo(int imageId, imageDataQuery query)
	{

			try
			{
				//opens connection with client
		        WebResource resource = client.resource(URL+"/images");

		        //Adds parameters to be posted
		        FormDataMultiPart form = new FormDataMultiPart();
		        //Logic check to determine what is posted to the image
		        if(query.getAltText()!= "")
		        form.field("altText",query.getAltText());
		        if(query.getDescription()!="")
		        form.field("description",query.getDescription());
		        if(query.getOrganisms()!=null)
		        form.field("organisms",query.getOrganisms().toString());
		        
		        //Method specific addition of the image id
		        form.field("id", Integer.toString(imageId));
		        ClientResponse response = resource.type(MediaType.MULTIPART_FORM_DATA).put(ClientResponse.class, form);
		        System.out.println(response.toString());
			}
			catch(HTTPException e)
			{
				System.out.println("The image id you have provided does not exist. Please enter a valid image Id.");
			}
	}

	//Adds an image, file path is required.
	//Uses FormDataMultiPart due to the special parameter of a file, and Query was not equipt to handle the challenge
	//FormDataMultiPart is also used in PUT since they share many of the same mechanics.
	public void addImage(String filepath, imageDataQuery query)
	{
		try
		{
			//opens connection with client
	        WebResource resource = client.resource(URL+"/images");

	        //Adds parameters to be posted
	        FormDataMultiPart form = new FormDataMultiPart();
	        File file = new File(filepath);
	        //Logic check to determine what is posted to the image
	        if(query.getAltText()!= "")
	        form.field("altText",query.getAltText());
	        if(query.getDescription()!="")
	        form.field("description",query.getDescription());
	        if(query.getOrganisms()!=null)
	        form.field("organisms",query.getOrganisms().toString());
	        form.bodyPart(new FileDataBodyPart("image", file, MediaType.MULTIPART_FORM_DATA_TYPE));
	        ClientResponse response = resource.type(MediaType.MULTIPART_FORM_DATA).post(ClientResponse.class, form);
	        System.out.println(response.toString());
		}
		catch(HTTPException e)
		{
			System.out.println("The image id you have provided does not exist. Please enter a valid image Id.");
		}
	}
	
	//Deletes the image
	//Side note, I had to use the old DELETE, I was getting bad request callbacks.
	public void deleteImage(int id)
	{
		try
		{
			//opens connection with client
			ClientConfig cc = new DefaultClientConfig();
	        Client client = new ApacheHttpClient();
	        WebResource resource = client.resource("http://192.168.142.128/api/images");
	        FormDataMultiPart form = new FormDataMultiPart();

	        form.field("id",Integer.toString(id));


	       resource.type(MediaType.MULTIPART_FORM_DATA).delete(form);

	       System.out.println("Image "+Integer.toString(id)+" has been deleted successfully!");
		}
		catch(HTTPException e)
		{
			System.out.println("The image id you have provided does not exist. Please enter a valid image Id.");
		}
		
	}
}