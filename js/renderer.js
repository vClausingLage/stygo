const scene = new THREE.Scene()
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 )

const renderer = new THREE.WebGLRenderer()
renderer.setSize( window.innerWidth, window.innerHeight )
document.body.appendChild( renderer.domElement )

const geometryOne = new THREE.SphereGeometry( 10,32,16 )
const material = new THREE.MeshStandardMaterial( { color: 0xfeeff } )
const sphereOne = new THREE.Mesh( geometryOne, material )
scene.add( sphereOne )
sphereOne.position.x = 40

const geometryTwo = new THREE.SphereGeometry( 20,32,16 )
const sphereTwo = new THREE.Mesh( geometryTwo, material )
scene.add( sphereTwo )
sphereTwo.position.x = 10

// const light = new THREE.AmbientLight( 0xffffff ); // soft white light
// scene.add( light );

const pointLight = new THREE.PointLight(0xffffff)
pointLight.position.set(1,1,30)
scene.add(pointLight)

// Entfernung
camera.position.z = 50

// Render-Funktion
function animate() {
	requestAnimationFrame( animate )
	renderer.render( scene, camera )
}
animate();